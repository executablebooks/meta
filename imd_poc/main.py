import re
from typing import Dict, TextIO, Type, Union

import panflute as pf
import pyparsing as pp
import yaml

from imd_poc.chunks.base import BaseChunk
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


def process_doc(path: Union[str, TextIO], output_fmt: str):
    with open(path) as handle:
        # we add line breaks either side,
        # to make sure the multi-line regexes work
        content = new_content = "\n" + handle.read().rstrip() + "\n"

    # load the document metadata
    doc_metadata = {}
    meta_match = REGEX_DOCMETA.findall(content)
    if meta_match:
        doc_metadata = yaml.safe_load(meta_match[0])

    chunk_converters = {}  # type: Dict[str, BaseChunk]
    chunk_outputs = []
    # process chunks and insert placeholders
    # we do this before pandoc conversion, because pandoc does not support chunks
    # we do this in a try block, to ensure all converter are closed down
    try:
        for match in REGEX_CHUNK.finditer(content):
            chunk_type = match.group(1)
            # instantiate a converter for the type
            if chunk_type not in chunk_converters:
                chunk_cls = find_entry_point(
                    chunk_type, CHUNK_ENTRY_GROUP
                )  # type: Type[BaseChunk]
                chunk_converters[chunk_type] = chunk_cls(
                    output_fmt=output_fmt, doc_metadata=doc_metadata
                )  # TODO doc metadata
            # print(parse_chunk_options(match.group(2)))
            chunk_outputs.append(
                chunk_converters[chunk_type].process_chunk(
                    text=match.group(3), options=parse_chunk_options(match.group(2))
                )
            )
            new_content = (
                new_content[: match.start()]
                + f"\n```{'-'*(match.end() - match.start()-9)}\n```\n"
                + new_content[match.end() :]
            )
    finally:
        # call each converter to close down, e.g. if the are running a kernel
        for converter in chunk_converters.values():
            try:
                converter.clean_up()
            except:
                pass

    # parse document into pandoc AST
    doc = pf.convert_text(new_content, standalone=True)  # type; pf.Doc

    # insert chunk output back into documents
    doc_content = []
    for el in doc.content:
        if (
            isinstance(el, pf.CodeBlock)
            and el.classes
            and el.classes[0].startswith("-")
        ):
            output = chunk_outputs.pop(0)
            if output:
                doc_content.append(output)
        else:
            doc_content.append(el)
    doc.content = doc_content

    # TODO formatting of labels etc

    return doc
