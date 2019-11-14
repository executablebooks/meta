from panflute import CodeBlock, convert_text, Div, Doc, Para, Span
from panflute.tools import meta2builtin
from typing import Any, Callable, List, Mapping, TextIO, Tuple, Union
import yaml

from .definitions import (
    METADATA_CLASS,
    NEW_CELL_CLASS,
    RAW_CELL_CLASS,
    NB_CELL_CLASS,
    CELL_NUMBER_ATTR,
    CODE_CELL_CLASS,
)


class Imd2PandocAST:
    def __call__(self, path: Union[str, TextIO]) -> Doc:
        return self.parse(path)

    def insert_missing_meta(self, content):
        """In-place insertion of missing metadata."""
        missing_meta = CodeBlock("{}", classes=[METADATA_CLASS])
        content.insert(0, missing_meta)

    def parse(self, path: Union[str, TextIO]) -> Doc:
        """Parse the document."""

        # read document to pandoc AST
        doc = file_to_doc(path)

        # retrieve metadata
        doc_metadata = meta2builtin(doc.metadata)
        language_name = doc_metadata.get("language_info", {}).get("name", "python")
        kernel_name = doc_metadata.get("kernelspec", {}).get("name", "python3")

        # setup variables
        doc_content = []
        cell_content = []
        found_metadata = False
        cell_number = 1

        for element in doc.content:
            is_new_cell_span = False
            if isinstance(element, Para) and element.content:
                if (
                    isinstance(element.content[0], Span)
                    and NEW_CELL_CLASS in element.content[0].classes
                ):
                    is_new_cell_span = True
            if (
                isinstance(element, CodeBlock)
                and METADATA_CLASS in element.classes
                or is_new_cell_span
            ):
                if not found_metadata:
                    # add missing metadata element to previous cell
                    self.insert_missing_meta(cell_content)
                # save previous cell
                doc_content.append(
                    Div(
                        *cell_content,
                        attributes={CELL_NUMBER_ATTR: str(cell_number)},
                        classes=[NB_CELL_CLASS, "markdown"],
                    )
                )
                # start a new cell
                if isinstance(element, Para):
                    cell_content = []
                    found_metadata = False
                else:
                    cell_content = [element]
                    found_metadata = True
                cell_number += 1

            elif isinstance(element, CodeBlock) and {
                CODE_CELL_CLASS,
                RAW_CELL_CLASS,
            }.intersection(element.classes):

                # handle if a code cell, with no metadata, is before a markdown cell, also with no metadata
                if cell_content and not found_metadata or len(cell_content) > 1:
                    if not found_metadata:
                        self.insert_missing_meta(cell_content)
                    doc_content.append(
                        Div(
                            *cell_content,
                            attributes={CELL_NUMBER_ATTR: str(cell_number)},
                            classes=[NB_CELL_CLASS, "markdown"],
                        )
                    )
                    cell_number += 1
                    cell_content = []
                    self.insert_missing_meta(cell_content)
                elif not found_metadata:
                    self.insert_missing_meta(cell_content)
                cell_content.append(element)

                # add classes
                attributes = {CELL_NUMBER_ATTR: str(cell_number)}
                if CODE_CELL_CLASS in element.classes:
                    classes = [NB_CELL_CLASS, "code"]
                    attributes["kernel"] = kernel_name
                    attributes["language"] = language_name
                elif RAW_CELL_CLASS in element.classes:
                    classes = [NB_CELL_CLASS, "raw"]
                else:
                    classes = [NB_CELL_CLASS, "other"]

                doc_content.append(
                    Div(*cell_content, attributes=attributes, classes=classes)
                )
                # start a new cell
                cell_number += 1
                cell_content = []
                found_metadata = False
            else:
                cell_content.append(element)

        # deal with any remaining cell_content
        if cell_content:
            if not found_metadata:
                # add missing metadata element to previous cell
                self.insert_missing_meta(cell_content)
            # save previous cell
            doc_content.append(
                Div(
                    *cell_content,
                    attributes={CELL_NUMBER_ATTR: str(cell_number)},
                    classes=[NB_CELL_CLASS, "markdown"],
                )
            )

        doc.content = doc_content

        return doc


def doc_to_str(doc: Doc, fmt: str, extra_args: List[str] = (), standalone: bool = True):
    """Convert pandoc AST to str."""
    return (
        convert_text(
            doc,
            input_format="panflute",
            output_format=fmt,
            standalone=standalone,
            extra_args=extra_args or [],
        ).rstrip()
        + "\n"
    )


def file_to_doc(
    path: Union[str, TextIO],
    input_format: str = "markdown",
    extra_args: List[str] = (),
    standalone: bool = True,
):
    """Read document to pandoc AST."""
    with open(path) as handle:
        doc = convert_text(
            handle.read(),
            input_format=input_format,
            standalone=standalone,
            extra_args=extra_args or [],
        )
    return doc

