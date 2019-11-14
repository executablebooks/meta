import nbformat
from nbformat.notebooknode import NotebookNode
from typing import Any, Callable, Mapping, TextIO, Tuple, Union
import yaml

from .definitions import (
    CODE_CELL_CLASS,
    DEFAULT_NB_VERSION,
    METADATA_CLASS,
    NEW_CELL_CLASS,
    RAW_CELL_CLASS,
)


def mapping_to_dict(
    obj: Any, strip_keys: list = (), leaf_func: Union[Callable, None] = None
) -> dict:
    """Recursively convert mappable objects to dicts, including in lists and tuples.

    :param list[str] strip_keys: list of keys to strip from the output
    :param leaf_func: a function to apply to leaf values

    """

    if isinstance(obj, Mapping):
        return {
            k: mapping_to_dict(obj[k], strip_keys, leaf_func)
            for k in sorted(obj.keys())
            if k not in strip_keys
        }
    elif isinstance(obj, (list, tuple)):
        return [mapping_to_dict(i, strip_keys, leaf_func) for i in obj]
    elif leaf_func is not None:
        return leaf_func(obj)
    else:
        return obj


def parse_nb2imd(path: Union[str, TextIO]) -> str:
    """Parse notebook to the IMarkdown format."""
    nb = nbformat.read(path, as_version=DEFAULT_NB_VERSION)  # type: NotebookNode

    output_string = "---\n"
    output_string += yaml.safe_dump(
        mapping_to_dict(nb.metadata), default_flow_style=False
    )
    output_string += "---\n\n"

    code_language = nb.metadata.language_info.name
    last_cell_type = None

    for cell in nb.cells:

        # output cell metadata
        if cell.metadata:
            output_string += f"```{METADATA_CLASS}\n"
            output_string += yaml.safe_dump(
                mapping_to_dict(cell.metadata), default_flow_style=False
            )
            output_string += "```\n\n"
        elif cell.cell_type == "markdown" and last_cell_type == "markdown":
            # separate cells that do not have metadata in a more concise way
            output_string += f"[]{{.{NEW_CELL_CLASS}}}\n\n"

        if cell.cell_type == "markdown":
            output_string += cell.source.rstrip() + "\n\n"

        if cell.cell_type == "code":
            output_string += f"```{{.{code_language} .{CODE_CELL_CLASS}}}\n"
            output_string += cell.source.rstrip() + "\n"
            output_string += "```\n\n"

        if cell.cell_type == "raw":
            output_string += f"```{RAW_CELL_CLASS}\n"
            output_string += cell.source.rstrip() + "\n"
            output_string += "```\n\n"

        last_cell_type = cell.cell_type

    return output_string.rstrip() + "\n"
