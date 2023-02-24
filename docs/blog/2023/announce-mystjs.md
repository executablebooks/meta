---
myst:
  substitutions:
    cta: |
      :::{admonition} Learn more and get involved with MyST
      :class: tip

      - See our new website at [myst-tools.org](https://myst-tools.org).
      - Try the [MyST quickstart tutorial](https://myst-tools.org/docs/mystjs/quickstart).
      - Follow the Twitter handle [@myst_tools](https://twitter.com/myst_tools).
      - [Get involved at our GitHub organization](https://github.com/executablebooks).
      - [See the Executable Books team compass](https://compass.executablebooks.org) for more about out organization.
      :::
---
# Announcing MyST-JS: Bringing MyST to JavaScript and Jupyter

```{post} 2023-02-09
:author: EBP
```

MyST Markdown is an extensible, semantic, and community-driven flavor of markdown designed for scientific and computational narratives.
It was created for [Jupyter Book](https://jupyterbook.org), and has gained wide adoption in Python's [Sphinx documentation ecosystem](https://myst-parser.readthedocs.io/en/latest/sphinx/intro.html).

Over the years we have come to believe that MyST has the right technical and social foundation to serve as a truly community-driven, cross-platform standard for authoring scientific content.
In this post, we're happy to announce **MyST Markdown as a standalone project and standard from the Executable Books community**.

The rest of this post provides ideas on where this project is heading and fleshes out some details.
We are still exploring what is possible, and would love feedback about what you're excited about.

{{ cta }}

## What is MyST Markdown?

Two years ago, the Executable Books project was [awarded a grant from the Sloan Foundation](../2020-02-25-hello-world) to build open source tooling for authoring and reading computational narratives.
We focused our efforts around [Jupyter Book](https://jupyterbook.org), a tool for writing and sharing computational narratives as websites and PDFs.
This project was built on the [Sphinx ecosystem](https://www.sphinx-doc.org/en/master/), an open source community that is at the foundation of documentation tools with Python.

MyST, short for _Markedly Structured Text_, was designed to combine the fluid experience of writing [Markdown](https://commonmark.org/) with the programmable extensibility of [reStructuredText](https://docutils.sourceforge.io/rst.html).
We needed these properties in order to meet the needs of Jupyter users in research and scholarly communication.
From this starting point, MyST was designed with the following goals in mind:

- **Be extensible**: We wanted a flavor of markdown that had extensibility built in from the start. This way users could extend its functionality in an intentional and structured way.
- **Be easy to read**: This extra extensibility should come without sacrificing the simplicity and readability of CommonMark markdown syntax.
- **Be semantic and structured**: We believe that the future of scholarly communication involves semantic and well-structured data, and wanted MyST to have a clearly defined specification and underlying data structure that authors and readers could leverage to connect MyST documents with one another.
- **Be community driven**: We believe that standards for scholarly communication require community governance and leadership, rather than being driven by one stakeholder. We framed MyST and the Jupyter Book stack as a collaboration between many organizations and will develop open governance that follows [the principles of open scholarly infrastructure](https://openscholarlyinfrastructure.org/).

The first implementation of MyST was [the MyST Markdown Python parser](https://myst-parser.readthedocs.io), a parser that allows users to take advantage of Sphinx's powerful **directives** and **roles** syntax in building their documentation.

Over the years we have seen interest in MyST raise considerably - it allows authors and researchers to express themselves more efficiently than traditional source text languages like LaTeX.
MyST has also become [a staple in the Python documentation ecosystem](https://www.sphinx-doc.org/en/master/usage/markdown.html), and is the backbone of authoring content in [Jupyter Book](https://jupyterbook.org).

## Bringing MyST to JavaScript with a new partnership

Because the original parser for MyST is written entirely in Python (and strongly tied to Sphinx), we realized that it would be difficult for the impact of this implementation of MyST to make its way out of the Jupyter Book and Python communities.

As a result, we've been exploring how to _extend MyST markdown into JavaScript_, with the goal of integrating with new technical ecosystems and communities.
We believe this will grow the impact of MyST, and allow for new kinds of workflows around computational narratives.
The project is called [MyST-JS](https://myst-tools.org/docs/mystjs).

To drive this effort forward, we have [partnered with Curvenote](https://curvenote.com) to upstream their open-source documentation engine into the Executable Books community.
This effort is based [on their command line interface](https://curvenote.com/docs/cli), which was designed for building technical documentation and computational narratives with JavaScript.
It will become the backbone of **MyST-JS**, and moving forward will be maintained by the Executable Books community.
There is still much to do, but you can preview this work already at [js.myst-tools.org](https://myst-tools.org/docs/mystjs).

Here are a few major new steps summarizing this work over the coming months:

### MyST is now a top-level project in Executable Books

We'll treat MyST as another major effort of the Executable Books project, similar to Jupyter Book.
It will have its own strategy and goals.
Jupyter Book will remain a consumer of MyST markdown, and it will remain one of many stakeholders in the MyST ecosystem.

:::{admonition} A new website!
We have set up a dedicated site to describe the MyST project at [myst-tools.org](https://myst-tools.org).
:::

### MyST will have first-class support in JavaScript

The [MyST-JS project](https://github.com/executablebooks/mystjs) is written entirely in TypeScript, with the goal of being re-usable across more applications and interfaces.
It also allows us to leverage the vast ecosystem of JavaScript libraries and frameworks for communication.
For example, we can use [templating frameworks to export MyST documents to a variety of LaTeX publication formats](https://github.com/myst-templates), and leverage the [unifiedjs project](https://unifiedjs.com/) to make MyST documents even more structured and consumable as data.

:::{admonition} Learn more
You can find the documentation for MyST JS at [js.myst-tools.org](https://myst-tools.org/docs/mystjs). You can also find an [issue from Rowan discussing major new planned functionality here](https://github.com/executablebooks/meta/issues/838).
:::

### MyST will have a JupyterLab extension

By bringing MyST into JavaScript, we can integrate it directly with JupyterLab and other web-based Jupyter interfaces.
For example, the [`jupyterlab-myst`](https://github.com/executablebooks/jupyterlab-myst) extension brings native MyST rendering into JupyterLab including admonitions, cross-references, and figure numbering using `mystjs` as the document engine.

By using a single core engine in JavaScript, we can ensure that the live interactive experience in web clients (such as JupyterLab) is identical to the HTML generated for static viewing.
This goal would be very difficult to reach with a combination of Sphinx and JavaScript separately rendering static and live content.

:::{admonition} Learn more
Learn more about the `jupyterlab-myst` project at [`executablebooks/jupyterlab-myst`](https://github.com/executablebooks/jupyterlab-myst).
:::

### MyST will have an implementation-agnostic specification

We are creating a formal definition for MyST at [spec.myst.tools](https://myst-tools.org/docs/spec).
This will allow us to extend MyST's syntax through a community-driven enhancement proposal process, and allow implementations of MyST to bring in new syntax as they wish.
Modifications to this specification will follow a [MyST Enhancement Proposals process](https://github.com/executablebooks/myst-enhancement-proposals) (MEPs for short).
We are still working out the details of how this spec will be structured, and what the process looks like, so please provide feedback if you have ideas for how to build a healthy and inclusive process around the MyST language.

:::{admonition} Learn more
The [MyST Enhancement Proposals repository](https://github.com/executablebooks/myst-enhancement-proposals) has the latest information about the MEP process and any active MEPs.
:::

### MyST-JS will complement Jupyter Book and focus on articles

We think that MyST-JS and Jupyter Book will be able to complement one another in the use-cases they focus on.
The Jupyter Book project (and its Sphinx stack) are focused on building multi-page books and project documentation.
It will continue to lean heavily into the use-cases that [Sphinx](https://www.sphinx-doc.org/en/master/) was designed for.
It also has major functionality that is missing in MyST-JS (for example, full internationalization support and extensions).
We will continue to improve and maintain this stack (both as individual projects in the Sphinx ecosystem and as the Jupyter Book distribution).

The MyST-JS project will initially focus its efforts on a slightly different use-case: **scientific publishing usecases**, such as reproducible analyses meant for publication, and integration with publisher workflows like [JATS](https://en.wikipedia.org/wiki/Journal_Article_Tag_Suite) and [LaTeX](https://www.latex-project.org/).
It will likely grow into new kinds of published content as well, and we will see how far the "MyST in JavaScript" experience can get.
We also hope to see more third-party interfaces and services take advantage of MyST-JS for their own use-cases.

Over time, we will continue to explore the potential of both of these ecosystems.
As an implementation-agnostic markdown standard, users should be able to switch back and forth between MyST parsers with low friction.

## Formalizing organizational structure for the Executable Books project

Finally, we have begun [formally defining the organizational structure and governance](https://compass.executablebooks.org/) of the Executable Books project.
Our goal is to transition this from a small grant-funded team into a community-driven project that has multiple stakeholders as well as clear pathways for participation and leadership.
We will continue to refine these organizational practices moving forward, and invite you to join our efforts!
More on this effort in a subsequent update!

:::{admonition} Learn more
See [this GitHub issue](https://github.com/executablebooks/meta/issues/493) for a long list of ideas and suggested improvements to make as we formalize our processes and structure.
:::

## Get involved

We are incredibly excited about the impact that MyST and Jupyter Book have had, and equally excited about the new things we'll enable with MyST's new foray into the JavaScript community. If you are interested in these efforts, or want to share your ideas, [please reach out](https://github.com/executablebooks/meta/discussions). We look forward to what the coming years will bring.

{{ cta }}
