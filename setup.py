from setuptools import setup, find_packages

setup(
    name="imd-poc",
    author="Chris Sewell",
    packages=find_packages(),
    install_requires=["nbformat", "nbconvert", "pyyaml", "panflute", "pyparsing"],
    extras_require={"testing": ["pytest", "pytest-regressions", "pandas"]},
    entry_points={
        "imd.chunks": [
            "python = imd_poc.chunks.python:PythonChunk",
            "julia = imd_poc.chunks.julia:JuliaChunk",
            "note = imd_poc.chunks.note:NoteChunk",
        ]
    },
)
