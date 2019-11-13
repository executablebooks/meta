import os

from imd_poc.imd2pandoc import doc_to_str, file_to_doc
from imd_poc.pandoc2html import pandoc2html

DIRPATH = os.path.realpath(os.path.dirname(__file__))


def test_pandoc2html(file_regression):

    doc = file_to_doc(os.path.join(DIRPATH, "test_imd2pandoc", "test_imd2pandoc.md"))
    file_regression.check(pandoc2html(doc), extension=".html")

