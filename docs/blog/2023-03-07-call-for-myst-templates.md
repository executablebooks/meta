# Call for MyST Templates for Open Science

```{post} 2023-03-07
:author: Rowan Cockett, Steve Purves
:image: 1
:excerpt: 2
```

:::{admonition} Sign up for the Upcoming MyST Templates Tutorial Webinar
:class: important

Interested in porting your first LaTeX template to a MyST template? Join the upcoming webinar (15th March 2023 @ 4pm UTC) and get started (and maybe finished) building your template during the session.

The webinar is hosted by Rowan & Steve from Curvenote, and will be a 2 hour walk-through at an easy pace of how to markup an existing LaTeX template or document for use with the [MyST Markdown](https://mystmd.org) CLI.

[Sign up for the webinar here](https://www.eventbrite.ca/e/how-to-create-a-custom-latex-template-that-works-with-jupyter-tickets-535622720977).

Reading this post **after** the event? Watch the [recording on youtube](https://youtube.com/live/Bdd-_5YZQ8c).
:::

+++ {"tags":[],"part":"abstract"}

Imagine a future where preparing research papers for submission is _frictionless_, freeing up valuable time to focus on what really matters—advancing knowledge and communicating breakthroughs in your field. In this blog we will highlight how to generate professional submission-ready PDFs on demand, and — with your help — for practically any scientific journal in the world.

> Let’s remove the chore of formatting from the workload of scientists and researchers worldwide.

+++ {"tags":[]}

```{figure} images/myst-export-to-any-template.png
:name: seGB9FVdRJ
:align: center
:width: 100%

Use MyST Markdown to export to any *LaTeX* template. To change the template you are using, just change the template option in frontmatter!
```

+++ {"tags":[]}

## MyST Markdown Template Repository

We're excited to make a call for _LaTeX_ submissions to the new [MyST Template Repository](https://github.com/myst-templates). MyST templates allow any existing journal's _LaTeX_ template to be easily built directly from metadata and content in MyST Markdown documents. Let’s not stop at journal papers — this equally applies to book, thesis, research report, and article templates too!

Porting a journal template to MyST Template takes about an hour, depending on the number of options and other requirements a template has, but after that initial investment, anyone who uses it saves a huge amount of time in formatting their documents. Cutting out this continual rework can really make a difference at scale!

Templates on the repository are completely open, part of the [Executable Books Project](https://executablebooks.org), and can be accessed, forked, remixed and contributed to [via GitHub](https://github.com/myst-templates).

```{figure} images/myst-open-template-repository.png
:name: aryv4vJd91
:align: center
:width: 100%

The [MyST Templates Repository](https://github.com/myst-templates) is hosted as an organization on GitHub, where each repository within the organization is an independent template for one of the supported export targets. If you are familiar with *LaTeX* check out some of the existing template repositories to get an idea of how a template is made (e.g. [arxiv_two_column](https://github.com/myst-templates/arxiv_two_column), [volcanica](https://github.com/myst-templates/volcanica))
```

+++ {"tags":[]}

> A single MyST template takes about an hour to build from an existing journal provided example… and can have a significant positive impact on time saved on all future submissions made via MyST.

+++ {"tags":[]}

```{note}
**Call for MyST Templates**

With the [mystmd.org](https://mystmd.org) now launched (beta) 🚀 and publicly available, we are looking for *LaTeX* template submissions from the community.

Contributing a *LaTeX* template is simple:

1. Find an up-to-date *LaTeX* template for the venue or an example manuscript
2. Follow the guide for [Creating a Template](https://mystmd.org/docs/jtex/create-a-latex-template)
3. Publish your template to GitHub and [add it to the index listing on myst-templates/templates](https://mystmd.org/docs/jtex/contribute-a-template#list-your-template)

The template can stay on your GitHub account, making it easy for you to maintain and update. If this is likely to be a widely used template you might want to “donate” your contribution as a community-curated template, and transfer it to the `myst-templates` org — [read more about doing that here](https://mystmd.org/jtex/contribute-a-template#donate-your-template).

```

+++ {"tags":[]}

## How authors use MyST Templates

Once a template is added to the repository it automatically becomes available to **the entire research community** via the open source [mystmd.org](https://mystmd.org) software ecosystem. Any MyST Markdown document of notebook can be exported to a template using the frontmatter ([learn more](https://mystmd.org/docs/mystjs/quickstart-myst-documents)).

```yaml
---
exports:
  - format: pdf
    template: lapreprint
---
```

To find the templates available, use the `myst` [command line interface](https://mystmd.org/docs/mystjs/quickstart) to search through all known templates:

```shell
myst templates list --tex
```

```{figure} images/myst-list-templates.png
:name: H98th7foSc
:align: center
:width: 90%

The partial output of the `myst templates list` command. This list is set to grow so that command also allows filtering on template type (website, docx, tex, pdf) and tags allowing you to narrow down to templates of interest.
```

Authors can then also query a specific template for a rich description, and details on options, parts and requirements for a document build. This information is detailed and set up by the people who create the template, all aimed at making the process of getting to a submission-ready PDF as easy as possible.

Here’s the output for the `volcanica` journal template. This is displayed when an author types:

```shell
myst templates list --pdf volcanica
```

```{figure} images/myst-show-template-details.png
:name: wMu6uL9PxS
:align: center
:width: 100%

Listing information on a specific template makes it easy to see various parts and variables to use when exporting your document.
```

As you can see there is helpful and detailed information on the various parts and options that the template supports, making it easy to complete the document frontmatter to create the template.

```{important}
**Writing a paper Faster with MyST Markdown 📺**

Looking to use the MyST Markdown tools for your writing?

Get started easily by following the [quickstart tutorials](https://mystmd.org/guide/quickstart) or [watch our webinar in the tutorial](https://mystmd.org/guide/quickstart-myst-documents).

```

+++ {"tags":[]}

## Creating a MyST Template

Ok, so having seen how rich the interaction with MyST Template is for authors, you may be thinking that building these templates might be quite onerous. This is not the case! If you have some _LaTeX_ experience and have the template and sample (e.g. content provided by a journal) the process is straightforward.

There is a dedicated command line tool to help with the process — its called `jtex` — and it bends over backwards to help you create a MyST Template. Use it alongside the well-known `cookiecutter` tool to go from a clean slate to a local git repository that is ready to push.

To get started for real, follow the [Create a Template](https://mystmd.org/docs/jtex/create-a-latex-template) guide on [MyST Markdown](https://mystmd.org), as it covers the whole process. To show you a little of what’s in store, the image below shows the output from `jtex check` part way through a template build.

```{figure} images/jtex-build-templates-easily-cli.png
:name: FCFEq6PLCj
:align: center
:width: 100%

Output from `jtex check` part way through the process of creating a template. Here we’ve added various options and parts updating our `template.tex` and `template.yml`files along the way, but the two are not yet in sync. `jtex` gives us concise warnings and error messages to help resolve the issues. It’ll also want about missing packages from configuration and can even automatically `--fix` those.
```

Here `jtex` is warning us about incorrect and unused options, missing images as well an incomplete package manifest. Having these errors and warnings any time we type `jtex check` help to speed up the template creation process enormously, as it helps keep us keep track of changes we’re making to the configuration file `template.yml` and he main `template.tex` file, which needs to be in sync.

We are also seeing missing elements in the package manifest, which can be usually fixed automatically by typing `jtex check --fix`, `jtex` even scans all `tex`, `cls` and `sty` files you add to the `files` section of `template.yml` make sure that the packaging listing is correct, as it is used to ensure no duplicate packages are loaded later.

```{important}
**Contribute your first MyST template!**

We’re on a mission to build the largest repository of open journal templates in the world. One that can be used to easily build papers from content in MyST Markdown and Juptyer Notebooks.

Together let’s take the chore and re-work out of preparing a paper submission and make it possible to easily switch papers to alternate journal formats without wasting researchers’ time.

[Make a start on your first MyST Template](https://mystmd.org/jtex) and submit it to the listing, or make a start and reach out to the [MyST templates community](https://github.com/myst-templates) in an issue to get help in getting it over the line.

```

```{admonition} Sign up for the Upcoming MyST Templates Tutorial Webinar
:class: dropdown, tip

Interested in porting your first LaTeX template to a MyST template?

Join the upcoming webinar (15th March 2023 @ 4pm UTC) and get started (and maybe finished) building your template during the session.

The webinar is hosted by Rowan & Steve from Curvenote, and will be a 2 hour walk-through at an easy pace of how to markup an existing LaTeX template or document for use with [MyST Markdown](https://mystmd.org) CLI.

[Sign up for the webinar here](https://www.eventbrite.ca/e/how-to-create-a-custom-latex-template-that-works-with-jupyter-tickets-535622720977).

Reading this post **after** the event? Watch the [recording on youtube](https://youtube.com/live/Bdd-_5YZQ8c).
```
