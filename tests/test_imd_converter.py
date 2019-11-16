import os

import pytest

from imd_poc.main import process_doc
from imd_poc.utils import doc_to_str, document_chunks

DIRPATH = os.path.realpath(os.path.dirname(__file__))


@pytest.mark.parametrize(
    "output_fmt,output_ext", (("markdown", ".md"), ("html", ".html"), ("latex", ".tex"), ("rst", ".rst"))
)
def test_process_doc1(output_fmt, output_ext, file_regression):

    doc = process_doc(os.path.join(DIRPATH, "test.imd"), output_fmt)
    file_regression.check(doc_to_str(doc, output_fmt), extension=output_ext)


def test_document_chunks(file_regression):
    file_regression.check(document_chunks())