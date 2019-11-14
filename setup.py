from setuptools import setup, find_packages

setup(
    name="imd-poc",
    author="Chris Sewell",
    packages=find_packages(),
    install_requires=["nbformat", "nbconvert", "pyyaml", "panflute", "importlib_resources"],
    extras_require={"testing": ["pytest", "pytest-regressions", "pandas"]},
)
