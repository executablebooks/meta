# Project Pythia Hackathon: Transitioning from JupyterBook to MyST Markdown

```{post} 2024-06-14
:author: Rowan Cockett (Steering Council, Executable Books; Curvenote), Angus Hollands (Core Team, Executable Books; 2i2c)
:image: 1
:excerpt: 2
```

This last week members of the ExecutableBooks team attended the Pythia Cook-off 2024 hackathon to help support and introduce [MyST Markdown](https://mystmd.org) as the next generation infrastructure being used for Jupyter Book v2.

Project Pythia serves as an education and training hub for the geoscientific Python community, acting as the educational wing of the [Pangeo](https://pangeo.io/) initiative. It provides an extensive range of Python-centered learning resources that are open-source, community-owned, geoscience-focused, and of exceptional quality. These resources and tutorials or “Cookbooks” offer ways to onboard into the geoscientific Python ecosystem and demonstrate ways to process and understand vast amounts of numerical scientific data using tools that support open, reproducible science, while fostering an inclusive community of practice. The Project Pythia technical stack has been based on Jupyter Book, whose next release is undergoing significant development at the moment through the mystmd project. Members of the MyST team attended the hackathon and helped with onboarding, development of new features, and bug fixes throughout the week. It was an exciting event that showcased the power of the new tools that we aim to capture in this post.

## Cookbook Architecture

The Project Pythia architecture relies on a number of Jupyter Books in separate repositories under the “Project Pythia” GitHub organization. Each Cookbook is contributed to by different authors who bring their own approaches to collaboration. To elevate the resources and incorporate them into the Pythia brand, there is a custom theme (including headers, logos and footers) and these resources are brought together in a gallery where users can filter and sort the cookbooks. In addition, there is a [Foundations cookbook](https://foundations.projectpythia.org/landing-page.html) that lays out general practices and resources that are useful throughout the computational geoscience community, with tutorials on everything from Jupyter and GitHub to the specific tools that are commonly used.
The Project Pythia infrastructure team has faced several challenges in maintaining their infrastructure that has hindered the scalability of the project as well as the maintenance burden on the team:

Configuration Sharing
: Updating shared configuration elements like navigation and branding requires changes to each individual cookbook, creating a time-consuming process where the infrastructure team opens many similar pull-requests to each individual cookbook to update the site as a whole.

Maintenance Burden
: Customizing the theme for Pythia was completed using the Sphinx framework and inheritance of multiple themes, many of which have been changed over the past few years, and this has placed a high maintenance burden on the infrastructure team to keep everything up to date.

Content Reuse Limitations
: There is currently limited ability to reuse and reference content from the foundational resources across different cookbooks, and referencing a concept requires cookbook readers to jump out of one tutorial and into another (e.g. how to use Conda or Jupyter). There are also many shared components, such as license information, “how to cite this cookbook”, and managing readme updates.

Limited use of MyST in Cookbooks
: Currently there is limited use of any advanced features of MyST Markdown in the cookbook tutorials (e.g. admonitions, cross-references, etc.) as the main way to experience a cookbook is through JupyterLab, and the default renderer of Jupyter doesn’t interpret MyST Markdown (but [jupyterlab-myst](https://github.com/executablebooks/jupyterlab-myst) does!).

Throughout the week, the core ExecutableBooks team, [Curvenote](https://curvenote.com), and [2i2c](https://2i2c.org) helped address some of these constraints with the new mystmd tooling that we have been developing over the last several years.

## Architecture and Workflow

One of the most exciting aspects of the transition was that it was almost painless, we have gone to great lengths to ensure that content is supported and backwards compatible, and there were almost no content changes required. The transition of a cookbook was almost as easy as:

```bash
conda install mystmd
myst
```

Over the coming months we will roll out targeted upgrade routines for JupyterBook that understand and upgrade the `_config.yml`, but where we were this week was that required manual effort by the team. It was pleasantly surprising to see that this also fixed some issues out of the box!

:::{figure} ./images/pythia-jb-myst.png
A comparison of upgrading a JupyterBook to mystmd, which happened to fix a few issues out of the box. Courtesy of Jenny Wong.
:::

The reaction from the hackathon team members on the initial experience differences from JupyterBook to MyST were around the ease of getting started (4 characters!) and the speed of the live reload when editing content providing immediate feedback and improving the content development workflow.

The site architecture was hosted on GitHub Pages, under a new organization which allowed every page to have its own dedicated “folder” on the domain, including the main landing page. To set up the GitHub action required a single command (`myst init --gh-pages`), which helped to streamline the amount of effort that we all had to put into the upgrade.

## Centralized Configuration

Once a few of the cookbooks had been transferred over, we addressed some of the configuration reuse challenges that the project has faced. We created a shared repository with a single mystmd config file, that held information about licensing, logos, navigation and binder configuration. By centralizing configurations for the entire project through a new inheritance feature (extends field in myst.yml), we simplified the management overhead and ensured consistency across the site. This still required a redeploy of each site when the configuration changes, but no code changes were required.

```yaml
version: 1
extends:
pythia.yml
```

The `extends` functionality (docs) allows for centralized management of brand identity, navigation links, license, copyright, as well as configuring computational resources.

## Gallery

One of the main use cases of Pythia is centralizing, showcasing and organizing important work in a vast community. The main landing experience is having a filtered list of cookbooks that have tags, dependencies, and the tools that each resource uses or teaches; this gallery is critically important and is currently a Sphinx plugin.

The current plugin system for MyST is centered around exporting structured content (the MyST AST). It is not yet possible to use this extension system for customization of the theme, such that a custom theme requires a hard-fork of the [existing MyST Theme applications](https://github.com/executablebooks/myst-theme/tree/main/themes) and introduces the corresponding maintenance burden; this is something we are working towards improving. We also had conversations about the fact that the plugin system (docs) is centered around JavaScript, which has a higher barrier of entry to computational scientists who may be more familiar with Python. Over the week, we prototyped a Python bridge that allowed the core of the development of plugins to be developed using Python, including with live-reload on edit. This allowed for the development of a rudimentary gallery that started to meet Project Pythia’s needs. There are many additional developments that will be necessary, including filtering, sorting and tagging, which is work that we intend to make available as a core myst-theme component that others can use. The centralization of these components will hopefully have the benefit of making the advancements that Pythia has made available to a wider community.

:::{figure} ./images/pythia-gallery.png
Project Pythia Gallery powered by a plugin form mystmd, written in Python.
:::

## Integrated Computation

One of the principles of MyST is to make computation part of the reading and browsing experience; this is made possible by `thebe`, which can connect to JupyterLab, JupyterHub, BinderHub or JupyterLite and execute content and show results directly on the page. The Pythia project has dedicated computational resources, so spinning up a computer in the cloud is super fast and you can see the results directly where you are reading. All of this configuration is also shared centrally. Throughout the week we fixed a number of issues related to CORS, JupyterLite and discussed ways to make the launch experience more user friendly.

<figure>
<video src="https://github.com/executablebooks/meta/raw/main/docs/_static/videos/pythia-thebe.mp4" autoplay muted webkit-playsinline="true" playsinline loop style="max-width:100%"></video>
<figcaption>Integrated execution connecting to a custom Binder, with inline controls. Powered by Thebe.</figcaption>
<figure>

Many of the existing cookbooks use static images, however, another one of the sprints started exploring ways to integrate interactive graphics using Bokeh. This is something we are excited to see in mystmd, and have initial support for out of the box.

<figure>
<video src="https://github.com/executablebooks/meta/raw/main/docs/_static/videos/pythia-interactive.mp4" autoplay muted webkit-playsinline="true" playsinline loop style="max-width:100%"></video>
<figcaption>Interactive visualizations using Bokeh showing directly in mystmd.</figcaption>
<figure>

## Integrated Build-time Execution

Another feature of mystmd is the ability to execute and cache the results of a computation, many of which take a long time to run in this community. The mystmd machinery does an intelligent job of separating out your content changes from computational changes, ensuring that if you are updating the narrative text of a cookbook, you will continue to get instant previews of your work.

```bash
myst build --execute
```

We discussed improvements to make for surfacing errors and controlling configuration of the execute command, as well as ways to integrate this into the existing continuous integration tasks that ensure that these commands run in nightly builds.

## Magical References

Currently there is a huge amount of valuable content in the foundations cookbook including terms, workflows, cheat-sheets, and concepts that are immensely helpful resources for readers of every other cookbook in the ecosystem. The Pythia project already does a fantastic job of listing the prerequisites of a cookbook and refers back to concepts and tutorials in this resource. During the week we took this a step further by using the new `xref` feature in MyST which allows for rich hover previews from one resource to another. This allows the reader to, for example, hover over “conda” or any other term and see the information directly in context where they are reading, without losing their place or train of thought to understand a command, term or concept. The `xref` feature is only a few weeks old, see [enabling open science reuse](https://curvenote.com/blog/open-science-reuse) as an overview of the motivation and design; Project Pythia has been the first project to use this new feature and the community was excited about the possibilities.

:::{epigraph}

The rich cross-referencing features in MyST are really compelling as a reader, but maybe even more importantly, they open up new ways of thinking about authoring and reusing modular content. One of the goals of the Pythia Cookbook initiative is to build up a high-quality network of mutually-reinforcing tutorials and example workflows reflecting best practices across a diverse geoscience community. Basic orientation on methods, datasets, and tools that are developed in one Cookbook can be easily incorporated into narratives in other Cookbooks focussing on completely different science applications. This is software empowering community knowledge-sharing!

-- Brian Rose
:::

<figure>
<video src="https://github.com/executablebooks/meta/raw/main/docs/_static/videos/pythia-xref.mp4" autoplay muted webkit-playsinline="true" playsinline loop style="max-width:100%"></video>
<figcaption>Hover cross references from the Radar Cookbook to the Foundations.</figcaption>
<figure>

An exciting outcome of this feature was that it sparked a conversation on how to organize resources like glossaries, equations and cheat-sheets and expose them in different ways that can provide immediate value in other Pythia Cookbooks – as well as completely unrelated projects. The reuse that is possible from these tools has the potential to change practices and centralize some efforts documentation between and across adjacent communities.

## Project Pythia: A Pioneer in Adopting Jupyter Book 2

Project Pythia is the first project that ExecutableBooks is officially helping adopt "Jupyter Book 2" using MyST MD. This adoption is a significant step forward for the ExecutableBooks team as we prototype and test JupyterBook-2, which is powered by mystmd. During the hackathon, we shipped multiple new versions of MyST MD, continuously improving the tools and features based on real-time feedback from the cross-disciplinary teams. It was an _incredibly_ exciting event and a major milestone for our team in releasing the next generation of JupyterBook. Over the coming months we will continue to help support Project Pythia continue their transition to MyST md and collaboratively work on many of the improvements and fixes that are necessary for a full transition.

We hope that with the new features and streamlined architecture, Project Pythia is better positioned to continue providing high-quality educational resources for the geosciences community and generate best practices for reproducible science communication that can be widely adopted.

## Acknowledgements

Rowan (Curvenote) and Angus (2i2c) from the ExecutableBooks team attended the event for the entire week helping with MyST and ExecutableBooks ecosystem questions and providing development support. Curvenote contributed development cycles for `mystmd` and `thebe` throughout the event (Franklin and Steve, who are also on the ExecutableBooks team). Project Pythia is funded through the University at Albany (NSF award 2324302) and helped organize and facilitate the event; 2i2c provided tailored compute services and on-site support (NSF award 2324304); UCAR led the planning and logistics for the event (NSF award 2324303).

:::{seealso}
For more information about the full event, see the [2i2c blog post](https://2i2c.org/blog/2024/project-pythia-cookoff).
:::
