# Using MyST Markdown in JupyterLab

```{post} 2023-06-26
:author: Rowan Cockett, Angus Hollands, Steve Purves
:image: 1
:excerpt: 2
```

:::{admonition} Upcoming MyST Webinar
:class: important

Join the upcoming webinar (5th July 2023 @ 3pm UTC) and get started using MyST in JupyterLab and how it connects to other scientific writing workflows. The webinar is hosted by Rowan & Steve from [Curvenote](https://curvenote.com), and will be an hour walk-through of using [MyST in JupyterLab](https://github.com/executablebooks/jupyterlab-myst).

[Sign up for the webinar](https://www.eventbrite.ca/e/scientific-writing-in-jupyterlab-with-myst-markdown-tickets-666670598707) or [watch the recording on YouTube](https://youtube.com/live/12-Go9E2huQ) after.
:::

If you are using JupyterBook or MyST Markdown, you can now see your content directly in JupyterLab with the our new extension [`jupyterlab-myst`](https://github.com/executablebooks/jupyterlab-myst). In this post we will showcase `jupyterlab-myst` to enable rich parsing and rendering of MyST natively in JupyterLab, including:

1. rich authoring components like figures, hover cross-references, tabbed content, and admonitions;
2. including variables, interactive widgets, and graphs directly inside of Markdown cells in the notebook; and
3. capturing and displaying rich frontmatter.

```{figure} ./images/jupyterlab-myst.png
:align: center
:width: 100%

MyST extension in JupyterLab with a rich authoring experience, frontmatter and inline expressions.
```

To follow along with the tutorial you can install the plugin using pip and see the full [getting started guide](https://mystmd.org/guide/quickstart-jupyter-lab-myst):

```shell
pip install jupyterlab_myst
```

The plugin works best in the latest version of JupyterLab (version 4.0 or greater). We released v2 of our plugin on [June 23rd, 2023](https://github.com/executablebooks/jupyterlab-myst/releases/tag/v2.0.0), so if you have already installed the plugin, you can update to v2!

## Rendered MyST Markdown

The MyST extension for Jupyter is responsible for rendering markdown in every cell, you can add most of the directives and roles that you are used to from JupyterBook including callouts/admonitions, math, images, figures, proofs, exercises, cards, grids, tabs, and all sorts of other typography like footnotes, definition lists, and glossaries. For a complete guide on the supported MyST syntax see <https://mystmd.org/guide>.

When you have installed the extension open any notebook or markdown document, and the markdown will be rendered as MyST. For example, showing the rich frontmatter as well as an admonition in dark mode.

<figure>
<video src="https://github.com/executablebooks/meta/raw/d30cae55226c762a956c5a33cf9fd6e93557f3f8/docs/_static/videos/jupyterlab-markup-dark.mp4" autoplay muted webkit-playsinline="true" playsinline loop style="max-width:100%"></video>
<figcaption>Showing MyST Markdown rendering in dark mode!</figcaption>
</figure>

Some of the new additions that we added for v2 of the extension are:

- GitHub link previews for issues, pull-requests and code ([demo](https://mystmd.org/guide/external-references#issues-and-pull-requests))
- Wikipedia integrations to show hover-cards ([demo](https://mystmd.org/guide/external-references#wikipedia-links))
- Task lists that edit your markdown cells ([demo](https://mystmd.org/guide/quickstart-jupyter-lab-myst#task-lists))
- Rabbit-hole links for cross-referenced content ([demo](https://mystmd.org/guide/quickstart-myst-markdown#links-cross-references))
- Glossaries and terms ([demo](https://mystmd.org/guide/glossaries-and-terms))
- Support for proofs ([demo](https://mystmd.org/guide/proofs-and-theorems)) and exercises ([demo](https://mystmd.org/guide/exercises))
- Copy buttons on your presentational code ([demo](https://mystmd.org/guide/code#code-blocks))

These all work in your notebook cells as well as now opening a markdown document in preview.

<figure>
<video src="https://github.com/executablebooks/meta/raw/d30cae55226c762a956c5a33cf9fd6e93557f3f8/docs/_static/videos/jupyterlab-markdown-preview.mp4" autoplay muted webkit-playsinline="true" playsinline loop style="max-width:100%"></video>
<figcaption>Instant MyST Markdown preview for full markdown documents.</figcaption>
</figure>

## Inline Variables & Execution

JupyterLab MyST allows you to create and evaluate inline expressions using the `{eval}` role. These turn your markdown cells into places that you can quickly evaluate a simple expression, such as:

- The value of the variable `x`: `` {eval}`x` ``
- Expand a sympy equation `polynomial`: `` {eval}`expand(polynomial)` ``
- Add inline matplotlib “sparklines”
- Add ipywidgets directly inline for sliders and other dropdowns

<figure>
<video src="https://github.com/executablebooks/meta/raw/d30cae55226c762a956c5a33cf9fd6e93557f3f8/docs/_static/videos/jupyterlab-myst-inline.mp4" autoplay muted webkit-playsinline="true" playsinline loop style="max-width:100%"></video>
<figcaption>Inline execution in markdown cells using the <code>{eval}</code> role.</figcaption>
</figure>

Inline expressions open up a whole new world for communicating with interactive computation, and we are excited to explore this and other integrations with [thebe](https://github.com/executablebooks/thebe) and [JupyterLite](https://jupyterlite.readthedocs.io/en/latest/) in the coming months.

## Adding Rich Frontmatter

The first cell of your notebook is rendered as rich-metadata that includes your notebook title, subtitle, authors, affiliations, code license, and much more (see all [frontmatter options](https://mystmd.org/guide/frontmatter)). To render the frontmatter, simply include a YAML block in your first markdown cell:

```yaml
---
title: Working with MyST Markdown
subtitle: In JupyterLab
license: CC-BY-4.0
---
```

Having this content as data, rather than as custom HTML code is a big step up in FAIR and open-science practices as more Jupyter Notebooks adopt this over time. You can also use this part of your document to add [math macros](https://mystmd.org/guide/math#math-macros) and [abbreviations](https://mystmd.org/guide/glossaries-and-terms#abbreviations).

## Working with JupyterBook and other tools

One of the benefits of working in the JupyterLab ecosystem is the ability for plugins to work together in the ecosystem. Our main use cases is to support JupyterBook content, and most users are able to use the MyST plugin directly, improving the authoring experience as well as ensuring a closer experience between your rendered HTML book and any tutorials that your readers might open in Binder or on their local machine. If you have a directive or configuration that you want to see supported — [please reach out](https://github.com/executablebooks/meta/discussions)!

### Jupytext

You can also use your notebooks directly with Jupytext, by opening your markdown notebook using the existing Jupytext plugin directly in JupyterLab. Any `{code-cell}` directives will be turned into Jupyter code cells, and your MyST Markdown will be rendered as is!

### JupyterDesktop

You can also use MyST in JupyterDesktop, just install the extension as is and it works out of the box, allowing you to double click on a Notebook and get up and running with MyST.

<figure>
<video src="https://github.com/executablebooks/meta/raw/d30cae55226c762a956c5a33cf9fd6e93557f3f8/docs/_static/videos/jupyterlab-desktop.mp4" autoplay muted webkit-playsinline="true" playsinline loop style="max-width:100%"></video>
<figcaption>The MyST plugin works in JupyterLab Desktop as well! Thanks <a href="https://github.com/roaldarbol" target="_blank">Mikkel Roald-Arbøl</a> for testing this out and letting us know!</figcaption>
<figure>

## Next Steps

The `jupyterlab-myst` plugin is supported by our ongoing work of bringing MyST into JavaScript, which allows native MyST rendering directly in JupyterLab using [mystjs](https://github.com/executablebooks/mystjs) as the document engine. The MyST extension for Jupyter is still new, and if you come across any bugs, please [open an issue](https://github.com/executablebooks/jupyterlab-myst/issues) and we will try our best to fix it soon!

Our goal is to support as many of the extensions, roles, and directives in use in your JuptyerBooks. If you have ideas about other ways that we could make MyST more useful in JupyterLab, [let us know](https://github.com/executablebooks/meta/discussions).
