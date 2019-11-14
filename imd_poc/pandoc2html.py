import os
import tempfile

import importlib_resources
from panflute import Cite, Doc, Div, Para, RawBlock, RawInline, Space, Str, Emph
import yaml

from imd_poc.pandoc_exec import exec_code_cells
from imd_poc.imd2pandoc import doc_to_str
from imd_poc import resources


def process_references(cite: Cite, doc: Doc):
    """Turn citations into anchors."""
    if not isinstance(cite, Cite):
        return None
    return [
        RawInline(
            f'<a href="#{c.id}">{doc.labels[c.id]["type"]} {doc.labels[c.id]["number"]}</a>',
            format="html",
        )
        for c in cite.citations
    ]


def pandoc2html(doc: Doc, execute: bool = True):
    """Convert pandoc to HTML."""
    # execute cells
    if execute:
        exec_code_cells(doc)

    doc.labels = {}

    # Apply metadata
    for element in doc.content:
        if isinstance(element, Div):
            metadata_block = element.content.pop(0)
            metadata_imd = yaml.safe_load(metadata_block.text).get("imd", {})
            if "type" in metadata_imd:
                element.classes.append(str(metadata_imd["type"]))
            if "code" in element.classes and len(element.content) > 1:
                output_block = element.content.pop(1)
                outputs = yaml.safe_load(output_block.text)

                # use just first output for now
                output = outputs[0]
                if (
                    output["output_type"] == "execute_result"
                    and "text/html" in output["data"]
                ):
                    element.content.append(
                        RawBlock(output["data"]["text/html"], format="html")
                    )
                    if "label" in metadata_imd:
                        label = RawInline(
                            (
                                '<a id="{0}" class="anchor-link" name="#{0}" href="#{0}" '
                                'title="Permalink to this caption">¶</a>'
                            ).format(metadata_imd["label"]),
                            format="html",
                        )
                        doc.labels = {
                            metadata_imd["label"]: {
                                "type": metadata_imd.get("type", "figure").capitalize(),
                                "number": len(doc.labels) + 1,
                            }
                        }

                    else:
                        label = Str("")
                    if "caption" in metadata_imd:
                        element.content.append(
                            Div(
                                Para(
                                    Emph(
                                        Str(
                                            f"{metadata_imd.get('type', 'figure').capitalize()}:"
                                        ),
                                        Space,
                                        Str(f"{metadata_imd['caption']}"),
                                        Space,
                                        label,
                                    )
                                )
                            )
                        )
                    else:
                        element.content.append(Div(Para(label)))

    doc.walk(process_references, doc=doc)

    css = importlib_resources.read_text(resources, "html.css")
    css = f"<style>\n{css}\n</style>"

    _, filepath = tempfile.mkstemp()
    with open(filepath, "w") as handle:
        handle.write(css)
    try:
        string = doc_to_str(doc, "html", extra_args=[f"--include-in-header={filepath}"])
    finally:
        os.remove(filepath)

    return string
