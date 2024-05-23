# Towards Jupyter Book 2 with MyST-MD

```{post} 2024-05-19
:author: Angus Hollands, Rowan Cockett, Chris Holdgraf
:image: 1
:excerpt: 2
```

## Jupyter Book and MyST - A Success Story

Over [the past four years](https://executablebooks.org/en/latest/blog/2020-02-25-hello-world/), the [Executable Book(s)](https://executablebooks.org) (EB) project has been working to _improve workflows for writing and publishing with Jupyter Notebooks, along with the broader open source science ecosystem._

Within this collaboration, much of the development effort has been spent on building [Jupyter Book](https://jupyterbook.org/), [which has been a tremendous success](https://executablebooks.org/en/latest/blog/2023/new-project-members/); there are at least 13,209 GitHub repositories using the tool according to the [dependency graph for the project](https://github.com/executablebooks/jupyter-book/network/dependents).[^1] Furthermore, the reach of EB has grown to encompass documentation writers and package authors who use EB tools to provide a richer experience for their audiences. For example, six of the flagship scientific python projects[^scipy] like [NumPy](https://numpy.org/doc/stable/), [Pandas](https://pandas.pydata.org/docs/), and [Dask](https://docs.dask.org/en/stable/) make use of at least one of the Sphinx-based tools we’ve developed such as the [PyData Sphinx Theme](http://pydata-sphinx-theme.readthedocs.io), the [Sphinx Book Theme](http://sphinx-book-theme.readthedocs.io), [myst-parser](https://myst-parser.readthedocs.io), or the Jupyter Notebook parser [myst-nb](https://myst-nb.readthedocs.io).[^popular]

[^scipy]: Here, Scientific Python means something distinct from "scientific python". The former refers to a community project <https://scientific-python.org/>.
[^1]: These are repositories whose dependency information is sufficiently described such that GitHub is able to identify a dependency upon Jupyter Book. As such, the true figure may be higher.

[^popular]: See [https://hugovk.github.io/top-pypi-packages](https://hugovk.github.io/top-pypi-packages) for the list we used.

During this time, it has become clear that the [MyST Markdown language](https://executablebooks.org/en/latest/blog/2020-08-07-announce-book/#an-enhanced-flavor-of-markdown) has been at the heart of the project’s growth. In 2023, [this was recognised by designating MyST a top-level project](https://executablebooks.org/en/latest/blog/2023-02-09-announce-mystjs/#myst-is-now-a-top-level-project-in-executable-books) in Executable Books and launching the [MyST-MD](https://mystmd.org) (previously MyST-JS) in collaboration with [Curvenote](https://curvenote.com/). The JavaScript tools for parsing and rendering MyST Markdown on the web are now used by [JupyterLab MyST](https://github.com/executablebooks/jupyterlab-myst) to bring MyST Markdown to JupyterLab, and even [power the proceedings rendering at SciPy 2024](https://curvenote.com/news/curvenote-sponsors-scipy-proceedings-2024).

With MyST-MD, the project added a critical new capability: a **document structure and engine** in addition to the MyST markdown syntax. Rather than parsing MyST to Sphinx, MyST-MD provides its own [standard document format and structure](https://mystmd.org/spec/) (as JSON), and an [engine that exposes MyST documents](https://mystmd.org/guide) in a flexible and reusable way. With the `mystmd` command line interface (CLI), it is now possible to use MyST-MD to produce [scientific PDFs](https://mystmd.org/guide/creating-pdf-documents), [documents](https://mystmd.org/guide/creating-word-documents), and [websites](https://mystmd.org/guide/website-templates).

## Next steps for Jupyter Book

The `1.x` release cycle across the Jupyter Book packages conveys our belief that many of the Sphinx-based tools that power Jupyter Book, such as `myst-nb` and `myst-parser` have matured to a point of _stability_, and are _feature-complete_ for Jupyter Book’s goals.[^2]

[^2]: There is still plenty to improve in these tools for serving the open source developer community, and we anticipate that the maintainer community around them will continue to do so. Our definition of feature complete refers to meeting the needs of scientific and scholarly communication with Jupyter Book.

Looking forward, there are still clear areas of improvements for Jupyter Book, such as simplifying the PDF export process, lowering the barrier to extensibility, improving the UX for authoring with Jupyter interfaces, and publishing to a wider range of platforms (such as scientific journals). **For the next phase of Jupyter Book, we believe that the new MyST-MD document engine is the right foundation to build on.**

**Jupyter Book 2 will _be_ an opinionated distribution of MyST-MD.**

To continue to deliver on these aims and principles, we are building a new Jupyter Book experience on top of [MyST-MD](https://mystmd.org). Unlike Jupyter Book 1, which provides its own configuration and interface on top of Sphinx, Jupyter Book 2 will be an opinionated distribution of MyST-MD.

By building on top of MyST-MD, we hope that:

- Users will face lower barriers in producing high-quality PDF outputs (e.g. via [Typst PDF rendering](https://mystmd.org/guide/creating-pdf-documents#rendering-pdfs-with-typst)) and interactive websites.
- Users will more easily discover, connect, reuse, and remix books published using MyST-MD / Jupyter Book, for richer and more reproducible communication. For example, via [cross-book embedding](https://mystmd.org/guide/embed).
- Users will benefit from the latest developments in web tooling for interactive, rich, computational experiences across all of the MyST-tools e.g., JupyterLab, and the CLI.
- Users will have a clear separation between the single source of truth for configuration ([https://mystmd.org](https://mystmd.org)), and the book-focused guide for the Jupyter Book distribution ([https://jupyterbook.org](https://jupyterbook.org)).
- Developers will face a lower barrier to entry to contribute through the use of standards such as [unist](https://github.com/syntax-tree/unist) (see [this example of contributing a new feature](https://mystmd.org/guide/contribute-add-feature) to help you get started).
- Developers will spend more time on enhancements and less time on maintenance, due to a more modern and streamlined infrastructure stack and lower technical debt.
- Users and developers alike will have a tighter feedback loop through the centralised development of MyST and Jupyter Book.

### Incorporation under the Jupyter project

In order to more effectively focus our development efforts and ensure long-term sustainability, we intend to find a new organizational home for the MyST document engine, and focus Executable Books on the Sphinx-based ecosystem of tools for software developers. Our intention is to form a new sub-community within the [Jupyter Project](http://jupyter.org) to steward the MyST document engine. To follow along, see [this Jupyter Enhancement Proposal](https://github.com/jupyter/enhancement-proposals/pull/123) for creating a `jupyter-book` community within Jupyter.

## What this means for Jupyter Book v1 users

Our first priority is to make a transition to Jupyter Book v2 as frictionless as possible, by supporting v1 workflows and configuration where we can, and providing migration pathways for users (see the [principles we’re following for migration](https://github.com/executablebooks/mystmd/issues/1113) for more information). This will be a one-off, guided process that will produce a book that is _easier to maintain_ and _fully-compatible_ with MyST-MD.

Below are the major areas where we anticipate users needing to perform steps to migrate.

**Configuration.** Existing authors of Jupyter Books will need to migrate their books to the new `myst.yml` configuration format that replaces `config.yaml` and `_toc.yml`. This will be made easier using an interactive CLI tool that assists in performing the conversion.

**Directives and roles.** We aim to support most Sphinx-based directives and roles, but some may be deprecated or change their configuration. Jupyter Book 2 will provide an interactive CLI tool that upgrades legacy syntax to the latest [MyST standard](https://mystmd.org/spec), such as `glossary` directives. This should be a mostly automatic process; although the presence of Sphinx was generally invisible in Jupyter Book 1, there are some places where it was not possible to hide this from the user. Such cases will require some human intervention to upgrade.

**Functionality.** Broad functionality of Jupyter Book v2 should be nearly the same as v1, with additional capabilities as well. There may be some short-term regressions in functionality for less-used features, and we aim to grow these back over time as users request.

## What this means for Sphinx extension users


The [Executable Books](https://executablebooks.org) organization will remain the stewards of the Sphinx-based stack, and we anticipate continuing support and development of the Sphinx ecosystem of tools, likely with a focus on supporting the open source developer community rather than the broader “scientific communication” community. These projects are strongly supported by open-source contributors, and we hope that this continues alongside work from the Executable Books team. Some Executable Books tools will likely slow their development (e.g., [`MyST-NB`](https://myst-nb.readthedocs.io)), while more heavily-used tools will likely continue to evolve and improve (e.g., [`myst-parser`](https://myst-parser.readthedocs.io), which now powers a large part of the markdown experience in Sphinx).  We recognise that there is an on-going need for these tools, and will continue working to ensure their long-lived success for the developer community.

## How can I follow along?

We’re excited about these new directions for the MyST project, and welcome others to join the conversation or get involved improving these tools.

**For synchronous chat about the MyST engine:** See [our Discord chat room](https://discord.mystmd.org/).

**For asynchronous discussion about the MyST engine:** See the [Discussions forum in the mystmd repository](https://github.com/executablebooks/mystmd/discussions).

**For high-level information about the MyST engine:** See [mystmd.org](https://mystmd.org).

