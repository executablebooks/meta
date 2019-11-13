import os

from imd_poc.nb2imd import parse_nb2imd

DIRPATH = os.path.realpath(os.path.dirname(__file__))


def test_nb2imd(file_regression):
    with open(os.path.join(DIRPATH, "imd_test.ipynb")) as handle:
        output = parse_nb2imd(handle)

    file_regression.check(output, extension=".md")
