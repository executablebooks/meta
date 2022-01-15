# Tools we build

There are several major tools that we have developed, or are contributing to,
as a part of this project. This page describes a few major components.


## Jupyter Book

Jupyter Book is an open source project for building beautiful,
publication-quality books and documents from computational material.

Jupyter Book has the following main features:

* **[Write publication-quality content in markdown](https://jupyterbook.org/content-types/markdown.html)**. You can
  write in either Jupyter markdown, or an extended flavor of markdown with publishing features.
  This includes support for rich syntax such as citations and cross-references,
  math and equations, and figures.
* **[Write content in Jupyter Notebooks](https://jupyterbook.org/content-types/notebooks.html)**, allowing
  you to include your code and outputs in your book. You can also write
  notebooks entirely in markdown to execute when you
  build your book.
* **[Execute and cache your book's content](https://jupyterbook.org/content/execute.html)**. For `.ipynb` and
  markdown notebooks, execute code and insert the latest outputs into your book.
  In addition, cache and re-use outputs to be used later.
* **[Insert notebook outputs into your content](https://jupyterbook.org/content/executable/output-insert.html)**. Generate outputs
  as you build your documentation, and insert them in-line with your content across pages.
* **[Add interactivity to your book](https://jupyterbook.org/interactive/launchbuttons.html)**. You can
  toggle visibility of cells, connect with an online service like Binder,
  and include interactive outputs from Jupyter.
* **[Generate a variety of outputs](https://jupyterbook.org/start/build.html)**, including single- and multi-page websites,
  as well as PDF outputs.
* **[A command-line interface](https://jupyterbook.org/reference/cli.html)** to quickly generate your books with one
  command, like so: `jupyter-book build mybook/`

```{note}
Jupyter Book gets most of its functionality from the collection of open source tools
listed below. You can use each tool on its own for your own purposes, or bring them
together with Jupyter Book.
```

## MyST - Markedly Structured Text

([link to documentation](https://myst-parser.readthedocs.io))

MyST allows you to write Sphinx documentation entirely in markdown.
It is an attempt to have the best of both worlds: the flexibility
and extensibility of Sphinx with the simplicity and readability of Markdown.

MyST has the following main features:

* **[A markdown parser for Sphinx](https://myst-parser.readthedocs.io/en/latest/using/intro.html#parse-with-sphinx)**. You can write your entire
  Sphinx documentation in markdown.
* **[Call Sphinx directives and roles from within Markdown](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#syntax-directives)**,
  allowing you to extend your document via Sphinx extensions.
* **[Extended Markdown syntax for useful rST features](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#extended-block-tokens)**, such
  as line commenting and footnotes.
* **[A Sphinx-independent parser of MyST markdown](https://myst-parser.readthedocs.io/en/latest/using/use_api.html)** that can be extended
  to add new functionality and outputs for MyST.
* **[A superset of CommonMark markdown](https://commonmark.org/)**. Any CommonMark markdown
  (such as Jupyter Notebook markdown) is natively supported by the MyST parser.

## MyST-NB

([link to documentation](https://myst-nb.readthedocs.io/))

`MyST-NB` is an open source tool for working with Jupyter Notebooks in the
Sphinx ecosystem. It provides the following primary features:

* **[Parse ipynb files in Sphinx](https://myst-nb.readthedocs.io/en/latest/#installation)**. Directly convert Jupyter
  Notebooks into Sphinx documents.
* **[Execute and Cache your notebook content](https://myst-nb.readthedocs.io/en/latest/use/execute.html)**.
  Save time building your documentation without needing to commit your notebook outputs
  directly into `git`.
* **[Write MyST Markdown](https://myst-nb.readthedocs.io/en/latest/use/myst.html)**. MyST Markdown
  allows you to write Sphinx roles and directives in markdown.
* **[Insert notebook outputs into your content](https://myst-nb.readthedocs.io/en/latest/use/glue.html)**. Generate outputs
  as you build your documentation, and insert them across pages.
* **[Write Jupyter Notebooks entirely with Markdown](https://myst-nb.readthedocs.io/en/latest/use/markdown.html)**. You can
  define the structure of a notebook *in pure-text* making it more diff-able.

In addition, there are several options for controlling the look and feel of how your
notebooks are used in your documentation.

## Sphinx Book Theme

([link to documentation](https://sphinx-book-theme.readthedocs.io))

This is a lightweight Sphinx theme designed to mimic the look-and-feel of an
interactive book. It has the following primary features:

* **[Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)**
  for visual elements and functionality.
* **[Flexible content layout](https://sphinx-book-theme.readthedocs.io/en/latest/content-blocks.html)** that is inspired by beautiful online books,
  such as [the Edward Tufte CSS guide](https://edwardtufte.github.io/tufte-css/)
* **[Visual classes designed for Jupyter Notebooks](https://sphinx-book-theme.readthedocs.io/en/latest/notebooks.html)**. Cell inputs, outputs,
  and interactive functionality are all supported.
* **[Launch buttons for online interactivity](https://sphinx-book-theme.readthedocs.io/en/latest/launch.html)**. For pages that are built with
  computational material, connect your site to an online BinderHub for interactive content.


## Jupyter Cache

([link to documentation](https://jupyter-cache.readthedocs.io))

This packages provides a clear
[API](https://jupyter-cache.readthedocs.io/en/latest/using/api.html#use-api) and
[CLI](https://jupyter-cache.readthedocs.io/en/latest/using/cli.html#use-cli)
for staging, executing and cacheing Jupyter Notebooks. Although there are
certainly other use cases, the principle use case this was written for is
generating books / websites, created from multiple notebooks (and other
text documents), during which it is desired that notebooks can be auto-executed
only if the notebook had been modified in a way that may alter its code cell
outputs.


## Markdown-it-py

([link to documentation](https://markdown-it-py.readthedocs.io))

> Markdown parser done right. Fast and easy to extend.

`markdown-it-py` is a Python port of the very popular [markdown-it](https://github.com/markdown-it/markdown-it)
package. Its goal is to remain as close as possible to the `markdown-it` API and plugin spec.
Here are its main features:

- Follows the __[CommonMark spec](http://spec.commonmark.org/)__ for baseline parsing
- Configurable syntax: You can add new rules and even replace existing ones
- Pluggable: Adds syntax extensions to extend the parser (see the [plugin list](https://markdown-it-py.readthedocs.io/en/latest/plugins.html#md-plugins))
- High speed (see our [benchmarking tests](https://markdown-it-py.readthedocs.io/en/latest/other.html#performance))
- [Safe by default](https://markdown-it-py.readthedocs.io/en/latest/other.html#security)



## A collection of Sphinx extensions

In addition to these major tools described above, the EBP also maintains a number
of tools in the Sphinx ecosystem for writing beautiful online books and documents.
For example:

* [`sphinx-copybutton`](https://sphinx-copybutton.readthedocs.io/)
* [`sphinx-togglebutton`](https://sphinx-togglebutton.readthedocs.io/)
* [`sphinx-panels`](https://sphinx-panels.readthedocs.io/en/latest/)
