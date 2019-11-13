import os

from imd_poc.imd2pandoc import Imd2PandocAST, doc_to_str

DIRPATH = os.path.realpath(os.path.dirname(__file__))


def test_imd2pandoc(file_regression):

    parser = Imd2PandocAST()
    doc = parser(os.path.join(DIRPATH, "test_nb2imd", "test_nb2imd.md"))
    file_regression.check(doc_to_str(doc, "markdown"), extension=".md")

