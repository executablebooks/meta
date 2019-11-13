import os

from imd_poc.imd2pandoc import doc_to_str, file_to_doc
from imd_poc.pandoc_exec import exec_code_cells

DIRPATH = os.path.realpath(os.path.dirname(__file__))


def test_pandoc_exec(file_regression):

    doc = file_to_doc(os.path.join(DIRPATH, "test_imd2pandoc", "test_imd2pandoc.md"))
    exec_code_cells(doc)
    file_regression.check(doc_to_str(doc, "markdown"), extension=".md")

