import os
import tempfile

import importlib_resources
from panflute import Doc, Div, Para, RawBlock, Space, Str, Emph
import yaml

from imd_poc.pandoc_exec import exec_code_cells
from imd_poc.imd2pandoc import doc_to_str
from imd_poc import resources


def pandoc2html(doc: Doc, execute: bool = True):
    """Convert pandoc to HTML."""
    # execute cells
    if execute:
        exec_code_cells(doc)

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
                                    )
                                )
                            )
                        )

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
