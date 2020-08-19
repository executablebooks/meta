# Developement Tips and Tricks

This section provides some useful tips and tricks for development of projects within the Executable Book Project ecosystem.

## Working with Sphinx

The [sphinx development guide](https://www.sphinx-doc.org/en/master/develop.html) is also a useful resource for understanding how `Sphinx` works.

### Getting Access to the Sphinx Abstract Syntax Tree (AST)

Getting access to the `xml` representation of the abstract syntax tree (AST) is a very
important step in understanding how Sphinx has organised the document.

One way to get this information is from the `.doctree` directory contained in a project `_build` directory.

Once you have built a sample project you can get access to the AST by loading the pickled
doctree in `python`:

```python
import pickle
doc = pickle.load(open("_build/.doctrees/<file>", "rb"))
```

to get the pseudo-xml representation used for test purposes

```python
pseudoxml = doc.pformat()
```

and to get a full `xml`

```python
xml = doc.asdom().toprettyxml()
```
