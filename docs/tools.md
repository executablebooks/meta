# Ecosystem of tools

There are several major tools that we have developed, or are contributing to,
as a part of this project. This page describes a few major components.

(tools:myst)=
## MyST Markdown

> An extensible, semantic, and community-driven flavor of markdown designed for scientific and computational narratives.

MyST Markdown is a language- and implementation-agnostic flavor of markdown with support from several tools (some of which are stewarded by us and listed below).

- [`myst-tools.org`](https://myst-tools.org) is a landing page about the project.
- [`spec.myst-tools.org`](https://spec.myst-tools.org) describes the MyST specification.
- [MyST Enhancement Proposals](https://github.com/executablebooks/myst-enhancement-proposals) a process for proposing and deciding on modifications to the MyST specification.

See below for examples of implementations and tools that use MyST Markdown.

(tools:jupyter-book)=
## Jupyter Book

> A command-line interface for building beautiful, publication-quality books and documents from computational content.

Jupyter Book is a distribution of [Sphinx](https://www.sphinx-doc.org/en/master/) that allows you to write content in markdown and Jupyter Notebooks, execute content and insert it into your book, and build a variety of outputs for interactivity and document publishing.

- [`jupyterbook.org`](https://jupyterbook.org) is the landing page about the project.
- [`gallery.jupyterbook.org`](https://executablebooks.org/en/latest/gallery) is a gallery of Jupyter Books that community members have submitted.
- [`executablebooks/jupyterbook`](https://github.com/executablebooks/jupyter-book) is our repository where you can contribute and open issues.

Jupyter Book gets most of its functionality from the collection of open source tools in [Python](tools:python) and [Sphinx](tools:sphinx) that are listed below.
You can use each tool on its own for your own purposes, or bring them together with Jupyter Book.

(tools:sphinx)=
## Sphinx stack

The core of this project's initial efforts.
These are a collection of tools that rely on [Sphinx's documentation engine](https://www.sphinx-doc.org/en/master/) for creating computational narratives.

### MyST - Markedly Structured Text

([link to documentation](https://myst-parser.readthedocs.io))

> A Sphinx parser for MyST Markdown. MyST allows you to write Sphinx documentation entirely in markdown.

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

### MyST-NB

([link to documentation](https://myst-nb.readthedocs.io/))

> A Sphinx extension for executing and reading Jupyter Notebooks with MyST Markdown.
 
It provides the following primary features:

* **[Parse ipynb files in Sphinx](https://myst-nb.readthedocs.io/en/latest/#installation)**. Directly convert Jupyter
  Notebooks into Sphinx documents.
* **[Execute and Cache your notebook content](https://myst-nb.readthedocs.io/en/latest/computation/execute.html)**.
  Save time building your documentation without needing to commit your notebook outputs
  directly into `git`.
* **[Write MyST Markdown](https://myst-nb.readthedocs.io/en/latest/authoring/basics.html#myst-markdown)**. MyST Markdown
  allows you to write Sphinx roles and directives in markdown.
* **[Insert notebook outputs into your content](https://myst-nb.readthedocs.io/en/latest/render/glue.html)**. Generate outputs
  as you build your documentation, and insert them across pages.
* **[Write Jupyter Notebooks entirely with Markdown](https://myst-nb.readthedocs.io/en/latest/authoring/text-notebooks.html)**. You can
  define the structure of a notebook *in pure-text* making it more diff-able.

In addition, there are several options for controlling the look and feel of how your
notebooks are used in your documentation.

### Sphinx Book Theme

([link to documentation](https://sphinx-book-theme.readthedocs.io))

> A lightweight Sphinx theme designed to mimic the look-and-feel of an interactive book.

It has the following primary features:

* **[Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)**
  for visual elements and functionality.
* **[Flexible content layout](https://sphinx-book-theme.readthedocs.io/en/latest/content/content-blocks.html)** that is inspired by beautiful online books,
  such as [the Edward Tufte CSS guide](https://edwardtufte.github.io/tufte-css/)
* **[Visual classes designed for Jupyter Notebooks](https://sphinx-book-theme.readthedocs.io/en/latest/content/notebooks.html)**. Cell inputs, outputs,
  and interactive functionality are all supported.
* **[Launch buttons for online interactivity](https://sphinx-book-theme.readthedocs.io/en/latest/content/launch.html)**. For pages that are built with
  computational material, connect your site to an online BinderHub for interactive content.

### A collection of Sphinx extensions

In addition to these major tools described above, the EBP also maintains a number
of tools in the Sphinx ecosystem for writing beautiful online books and documents.
For example:

* [`sphinx-copybutton`](https://sphinx-copybutton.readthedocs.io/)
* [`sphinx-design`](https://sphinx-design.readthedocs.io/en/latest/)
* [`sphinx-togglebutton`](https://sphinx-togglebutton.readthedocs.io/)
* [`sphinx-autobuild`](https://github.com/executablebooks/sphinx-autobuild)

(tools:python)=
## Python stack

These are tools written in Python but meant to be re-used across many projects.

### Jupyter Cache

> Allows you to execute and cache notebook files so that you only re-run them when you need to.

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

### Markdown-it-py

([link to documentation](https://markdown-it-py.readthedocs.io))

> A markdown parser done right. Fast and easy to extend.

`markdown-it-py` is a Python port of the very popular [markdown-it](https://github.com/markdown-it/markdown-it)
package. Its goal is to remain as close as possible to the `markdown-it` API and plugin spec.
Here are its main features:

- Follows the __[CommonMark spec](http://spec.commonmark.org/)__ for baseline parsing
- Configurable syntax: You can add new rules and even replace existing ones
- Pluggable: Adds syntax extensions to extend the parser (see the [plugin list](https://markdown-it-py.readthedocs.io/en/latest/plugins.html#md-plugins))
- High speed (see our [benchmarking tests](https://markdown-it-py.readthedocs.io/en/latest/other.html#performance))
- [Safe by default](https://markdown-it-py.readthedocs.io/en/latest/other.html#security)


## JavaScript stack

### MyST-JS

> A JavaScript implementation of MyST Markdown, and a command-line interface for building articles and technical documents for computational narratives.

- [link to repository](https://github.com/executablebooks/mystjs)
- [link to documentation](https://myst-tools.org/docs/mystjs)

### Thebe

> A JavaScript library that allows you to convert static code blocks into interactive and executable blocks.

It leverages [mybinder.org](https://mybinder.org) or [jupyterlite](https://jupyterlite.readthedocs.io).

- [link to repository](https://github.com/executablebooks/thebe).
- [link to documentation](https://thebe.readthedocs.io).

### jupyterlab-myst

A JupyterLab extension that allows users to write MyST Markdown in Jupyter Notebooks via JupyterLab.

- [link to repository](https://github.com/executablebooks/jupyterlab-myst).
