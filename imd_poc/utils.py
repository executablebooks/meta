import pkg_resources
from typing import List, TextIO, Union, Mapping, Callable, Any

from panflute import convert_text, Doc
import yaml


def find_entry_point(name, group, preferred=None):
    """find an entry point by name and group

    Parameters
    ----------
    name: str
        name of entry point
    group: str
        group of entry point
    preferred: str
        if multiple matches are found, prefer one from this module

    """
    entry_points = list(pkg_resources.iter_entry_points(group, name))
    if len(entry_points) == 0:
        raise pkg_resources.ResolutionError(
            "The {0} entry point " "{1} could not be found".format(group, name)
        )
    elif len(entry_points) != 1:
        # default to the preferred package
        oentry_points = []
        if preferred:
            oentry_points = [
                ep for ep in entry_points if ep.module_name.startswith(preferred)
            ]
        if len(oentry_points) != 1:
            raise pkg_resources.ResolutionError(
                "Multiple {0} plugins found for "
                "{1}: {2}".format(group, name, entry_points)
            )
        # logger.info(
        #     "Multiple {0} plugins found for {1}, "
        #     "defaulting to the {2} version".format(group, name, preferred)
        # )
        entry_point = oentry_points[0]
    else:
        entry_point = entry_points[0]
    return entry_point.load()


def document_chunks():
    """Gather all entry points and extract documentation."""
    outputs = {}
    for entry_point in pkg_resources.iter_entry_points("imd.chunks"):
        try:
            entry_cls = entry_point.load()
            outputs[entry_point.name] = {
                "description": entry_cls.__doc__,
                "formats": entry_cls.declare_formats(),
                "options": entry_cls.declare_options()
            }
        except:
            pass
    return yaml.safe_dump(outputs, default_flow_style=False)


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
