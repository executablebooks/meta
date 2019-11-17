import re
from textwrap import dedent
from typing import Dict, TextIO, Type, Union

import panflute as pf
from panflute.tools import meta2builtin
import pyparsing as pp
import yaml

from imd_poc.chunks.base import BaseChunk, ChunkResult
from imd_poc.utils import file_to_doc, find_entry_point

REGEX_DOCMETA = re.compile(
    r"(?:\n|\r\n?)---\s*(?:\n|\r\n?)(.+)(?:\n|\r\n?)---\s*(?:\n|\r\n?)", re.DOTALL
)
CHUNK_ENTRY_GROUP = "imd.chunks"
# TODO for some reason this isn't working with \s* before the final linebreak
REGEX_CHUNK = re.compile(
    r"(?:\n|\r\n?)\`\`\`\{([a-zA-Z]+)([^(?:\n|\r\n?)]*)\}\s*(?:\n|\r\n?)([^?!\`\`\`]*)\`\`\`(?:\n|\r\n?)",
    re.DOTALL,
)
CHUNK_CLASS = "imd-chunk"
REF_ENTRY_GROUP = "imd.references"
REGEX_REFERENCE = re.compile(r"@(.+)\(([^\)]+)\)")
REGEX_VARIABLE = re.compile(r"^\{\{([^\:]+)\:(.*)\}\}$")


def process_doc(path: Union[str, TextIO], output_fmt: str):
    with open(path) as handle:
        # we add line breaks either side,
        # to make sure the multi-line regexes work
        content = "\n" + handle.read().rstrip() + "\n"

    # reformat chunks into `pandoc.Div`s
    # we do this before pandoc conversion, because pandoc does not inherently support chunks,
    # but ideally there would be better pandoc integration
    while True:
        try:
            match = next(REGEX_CHUNK.finditer(content))
        except StopIteration:
            break
        chunk_type = match.group(1)
        options = parse_chunk_options(match.group(2))
        chunk_content = match.group(3)
        # note textwrap dedent doesn't seem to work properly
        new_block = f"""\
:::{{.{CHUNK_CLASS} type={chunk_type}}}
```options
{yaml.safe_dump(options)}
```
```content
{chunk_content}
```
:::
"""
        content = (
            content[: match.start()]
            + "\n\n"
            + new_block
            + "\n\n"
            + content[match.end() :]
        )

    # parse document into pandoc AST
    doc = pf.convert_text(content, standalone=True)  # type; pf.Doc
    doc.format = output_fmt
    doc.builtin_meta = meta2builtin(doc.metadata)
    doc.chunk_converters = {}  # type: Dict[str, BaseChunk]
    doc.chunk_data = {}

    # process chunks
    # we do this in a try/finally block, to ensure all 'opened' converters are cleaned up,
    # if an error is raised
    try:
        doc.walk(process_chunks)
    finally:
        # call each converter to clean up, e.g. close running a kernels
        for converter in doc.chunk_converters.values():
            try:
                converter.clean_up()
            except:
                pass

    doc.walk(format_references)

    return doc


def convert_value(value):
    """Convert a string value to a JSON type."""
    if value in ["False", "FALSE", "false"]:
        return False
    if value in ["True", "TRUE", "true"]:
        return True
    if value.startswith('"') or value.startswith("'"):
        return value[1:-1]
    try:
        return int(value)
    except:
        try:
            return float(value)
        except:
            pass
    return value


def parse_chunk_options(string: str) -> dict:
    """Parse the chunk options """
    label = pp.Word(pp.alphas)
    key = pp.Word(pp.alphas + "_.")
    value = pp.Or(
        [pp.Word(pp.alphanums + "_.-"), pp.sglQuotedString(), pp.dblQuotedString()]
    )
    comma, equals = map(pp.Suppress, ",=")
    # TODO handle identifier (the commented out code does not handle `{python eval=1}`)
    # pp.Optional(label ^ label + comma ^ comma)
    pattern = pp.Optional(pp.delimitedList(pp.Group(key + equals + value)))

    results = pattern.parseString(string)
    output = {}
    # if results and isinstance(results[0], str):
    #     output["id"] = results.pop(0)
    for part in results:
        output[part[0]] = convert_value(part[1])

    # TODO un-flatten dictionary? e.g. {fig.cap: 1} -> {fig: {cap: 1}}

    return output


def process_chunks(el: pf.Element, doc: pf.Doc):
    """Process a chunk."""

    if isinstance(el, pf.Div) and CHUNK_CLASS in el.classes:
        chunk_type = el.attributes["type"]
        options = yaml.safe_load(el.content[0].text)
        content = el.content[1].text
        if chunk_type not in doc.chunk_converters:
            chunk_cls = find_entry_point(
                chunk_type, CHUNK_ENTRY_GROUP
            )  # type: Type[BaseChunk]
            doc.chunk_converters[chunk_type] = chunk_cls(
                output_fmt=doc.format, doc_metadata=doc.builtin_meta
            )
        result = doc.chunk_converters[chunk_type].process_chunk(
            text=content, options=options
        )  # type: ChunkResult
        doc.chunk_data[chunk_type] = result.metadata
        return result.block

    if isinstance(el, pf.Str):
        match = REGEX_VARIABLE.match(el.text)
        if match and "variables" in doc.chunk_data.get(match.group(1), {}):
            replace = doc.chunk_data[match.group(1)]["variables"].get(match.group(2), None)
            if replace is not None:
                return pf.Str(str(replace))

def format_references(el: pf.Element, doc: pf.Doc):
    if not isinstance(el, pf.Str):
        return
    replacements = []
    for match in REGEX_REFERENCE.finditer(el.text):
        ref_type = match.group(1)
        refs = match.group(2)
        ref_cls = find_entry_point(ref_type, REF_ENTRY_GROUP)(
            output_fmt=doc.format, doc_metadata=doc.metadata
        )
        replacements.append(
            (ref_cls.process_reference(refs, {}), match.start(), match.end())
        )
    if replacements:
        # TODO handle if the replacement is not the the entire string,
        # or if there are multiple references
        return replacements[0][0]

