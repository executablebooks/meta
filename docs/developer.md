# Development Tips and Tricks

This section provides some useful tips and tricks for development of projects within the Executable Book Project ecosystem.

## Documentation resources

### Minifying images

We recommend minifying images whenever adding them to documentation.
This helps keep our repository size down, as well as the page load times of our documentation.
There are many minifying services out there, but [the `squoosh.app` service](https://squoosh.app/) is a lightweight and easy-to-use option.

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
