# Executable Books Update (October 2022)

```{post} 2022-11-16
:author: Matt McKay
```

This blog post provides an annual update for the Executable Books community. This post is an adaptation of an interim report provided to the Alfred P. Sloan Foundation. It shares how the project has been progressing relative to the initial grant success metrics, and concludes with a few comments about the future of Executable Books and our vision for the next 12 months.

We thank the Alfred P. Sloan Foundation for funding this work.

## Goals and Metrics

The project goal was to "build, enhance and promote a new path to document creation and publishing for next-generation textbooks and lectures."

The agreed success metrics were:

1.  Substantial enhancements to at least 3 existing open source projects
    that will form part of the toolchain.
2.  Expand the functionality of Jupyter Book to provide a convenient and
    high quality user interface.
3.  At least two lecture series from QuantEcon and at least one text
    from Caporaso Lab that are built entirely from these tools.
4.  At least three software contributors by end of grant who are not
    paid by grant funds.
5.  Adoption by at least 5 additional authors of computational science
    textbooks / lecture series.

In the next section we discuss progress towards these goals as of September 2022. While **all success metrics have already been met or surpassed**, remaining challenges include community building, sustainability, feature requests and documentation.

## Progress

The [Executable Book Project](https://executablebooks.org/en/latest/) (EBP) has developed very rapidly since its inception at the start of 2020. The EBP GitHub organisation now contains more than 75 repositories, which provide major enhancements to the core [Jupyter Book](https://jupyterbook.org/intro.html) (JB) infrastructure, as well as many Sphinx-compatible extensions that can be utilized by the broader Sphinx community. The [jupyter-book](https://github.com/executablebooks/jupyter-book) package receives over 59,000 downloads a month from `PyPI` (annual growth of 195%) and approximately five thousand downloads a month from `conda-forge`. It has collected more than 3,000 GitHub stars. More than 109 individuals have contributed commits to the main branch.

Jupyter Book has been widely adopted in academia and commercial settings. The [The Jupyter Book Gallery](https://executablebooks.org/en/latest/gallery.html), discussed below, has contributions from lecturers and researchers in psychology, computer science, economics, econometrics, computational mechanics, machine learning, genome sampling, network science, applied mathematics, epidemiology, history, image processing, computational chemistry, geography, particle physics, finance, thermodynamics and many other fields. The documentation for Google JAX, a package that is surging in popularity, is written with Jupyter Book.

The [MyST](https://github.com/executablebooks/myst-spec) flavor of Markdown, designed and developed by EBP to enable highly expressive scientific authoring, has also gained traction in a number of open source products. MyST is designed to be a multi-tool and multi-platform markup language, with parsing capabilities that facilitate its use in a variety of contexts. [MyST-parser](https://github.com/executablebooks/myst-parser) has a Sphinx extension that receives around 30,000 PyPI downloads a day (with  750K downloads last month), and is being widely adopted across the PyData ecosystem.

Below we provide further details on our progress vis-a-vis each individual success metric.

### Metric 1: Enhancements to Existing OS Projects

The metric in question is **substantial enhancements to at least 3 existing open source projects that will form part of the toolchain.**

In last year's interim report we highlighted *6 examples of substantial enhancements* to existing OS projects contributed by the EBP team.

Over the past year we have formed deeper partnerships with [Curvenote](https://curvenote.com) to accelerate the development of MyST support in javascript which has led to the [myst-js](https://github.com/executablebooks/mystjs) project.

### Metric 2: Expand the Functionality of Jupyter Book

The metric in question is **expand the functionality of Jupyter Book to provide a convenient and high quality user interface.**

EBP has made *very rapid, wide-ranging progress* in this area, building an authoring tool that facilitates open scientific writing in many contexts, as well as publishing high quality outputs in a variety of formats.

Below we review some of the changes from just the last 12 months.

**Scientific Writing:**

There have been significant contributions to all underlying core projects including major updates to [myst-parser](https://github.com/executablebooks/myst-parser) and [myst-nb](https://github.com/executablebooks/myst-nb)

The [myst-parser](https://github.com/executablebooks/myst-parser) has had three major releases in the past 12 months. On top of bug and ongoing maintenance updates some of the major changes include:

-   Support for the latest sphinx v5.
-   Improvements for markdown link resolution in MyST.
-   Bring support for `docutils` so rendering no longer requires sphinx
    which gives greater flexibility in developing rendering options.

The full changelog can be found [here](https://github.com/executablebooks/MyST-Parser/blob/master/CHANGELOG.md).

The [myst-nb](https://github.com/executablebooks/MyST-NB) has also had three major releases in the past 12 months. On top of bug and ongoing maintenance updates some of the major changes include:

-   Support for the latest sphinx v4 and v5.
-   Inclusion of multilevel configuration options to enable a hierachy
    of option parsing in a consistent way
-   Adding MIME render plugins for customised rendering options
-   Support for parallel execution
-   and many other improvements

The full changelog can be found [here](https://github.com/executablebooks/MyST-NB/blob/master/CHANGELOG.md).

**Maintainability:**

The [sphinx-book-theme](https://github.com/executablebooks/sphinx-book-theme) has been a focal point to refactor in the context of upstream projects in an effort to

-   reduce the maintenance burden by refactoring to minimize code
    duplications.
-   embrace a model of inheritence from upstream theme projects that it
    relies on.
-   work towards a user contributed theme writing guide to encourage
    community contributed themes.

**Teaching and Education:**

Tools have been updated this year, including [sphinx-exercise](https://github.com/executablebooks/sphinx-exercise), which has been completely re-written to support the addition of **exercise's** and **solution's** in books. This extension is also the first to introduce gated syntax to enable code execution within directives. While this **gated syntax** is not officially a MyST feature it will become one of the early MyST Enhancement Proposals (MEP) as we work to improve the Executable Books governance. 

**Interactivity:**

The core [thebe](https://github.com/executablebooks/thebe) project has been migrated to the executable books organisation. It powers much of the rich interactivity provided by `MyBinder` and the new `Jupyterlite` kernels.

A up-to-date list of Sphinx extensions can be found [on EBP](https://github.com/search?q=org%3Aexecutablebooks+sphinx-).

### Metric 3: QuantEcon and Caporaso Lap Conversions

The metric in question is *at least two lecture series from QuantEcon and at least one text from Caporaso Lab that are built entirely from these tools.*

This milestone has **been exceeded** as was documented in last years report, and we have continued to advance our work toward this metric this year.

Caporaso Lab has released another JupyterBook-based text, [QIIME 2 Cancer Microbiome Intervention Tutorial](https://docs.qiime2.org/jupyterbooks/cancer-microbiome-intervention-tutorial/), which was first developed to teach two online bioinformatics workshops, and is now available as a free text for cancer microbiome researchers. This book has a [corresponding online video course](https://www.youtube.com/playlist?list=PLbVDKwGpb3XmvnTrU40zHRT7NZWWVNUpt) which was developed with support from the National Cancer Institute, adding value to this project.

Caporaso Lab has begun work on a JupyterBook-based text, [The Four Corners Science and Computing Club (4CSCC) Lab Notebook](https://gregcaporaso.github.io/4cscc-ln/intro.html). This is being developed as a teacher's manual for integrating physical scientific computing exercises into pre-college classes based on the Raspberry Pi 400 platform, while the 4CSCC develops a corresponding workshop series. Ultimately the goal is that this will become a standalone resource. This work is funded in part by a Chan-Zuckberg Initiative Diversity, Equity, and Inclusion grant to Professor Caporaso, *Engaging Native American Students in Scientific Computing with QIIME 2*, a project focused on increasing representation of Native Americans in open source scientific computing.

Caporaso Lab added a full online video course paralleling Prof. Caporaso's *An Introduction to Applied Bioinformatics* (2nd edition). This work was not funded on this project, but adds value to content from Caporaso Lab that was reported last year.

Caporaso Lab continues to work on integration of JupyterBook into its QIIME 2 Library platform, and finalization of this work is planned for 2023. This will result in 10's of new JupyterBooks documenting QIIME 2 plugins.

### Metric 4: External Software Contributors

The metric in question is **at least three software contributors by end of grant who are not paid by grant funds.**

We have received contributions from _over 100 individuals_ outside of the grant-funded group. While most of these are smaller contributions, we continue to believe it is an important starting point to building a healthy community of contributors. Below is a brief summary of the contributors for each project as of today:

1.  Jupyter Book: [109 contributors](https://github.com/executablebooks/jupyter-book/graphs/contributors)
2.  Sphinx Book Theme: [44 contributors](https://github.com/executablebooks/sphinx-book-theme/graphs/contributors)
3.  MyST Parser: [32 contributors](https://github.com/executablebooks/MyST-Parser/graphs/contributors)
4.  MyST NB: [26 contributors](https://github.com/executablebooks/MyST-NB/graphs/contributors)

The number of external contributors continues to grow across the executable books projects.

If you would like to find out more about contributing, please get in touch and 
take a look at our [contributors guide](https://executablebooks.org/en/latest/contributing.html)


### Metric 5: Adoption by Additional Authors

The metric in question is **adoption by at least 5 additional authors of computational science textbooks / lecture series.**

Jupyter Book has been adopted by a large number of textbook authors across many different academic fields. A sample can be found at [The Jupyter Book Gallery](https://executablebooks.org/en/latest/gallery.html). This is a community-supported page where people can upload links to their Jupyter Books. As of this writing, there are *around 92 books* build using JB listed in the gallery.


## Future of Executable Books and Next Steps

Over the next 12 months the Executable Books project will have a focus on the sustainability of the project, including issue reduction and bug resolution and further community engagement and support. We are actively looking to grow external contributers to the project. 

We are also introducing some lightwieght governance structures including a *MyST Enhancement Proposal process (MEP)* to enable structured and transparent conversations about the future of the MyST syntax. MyST is becoming more widely adopted, with additional parser implementations. The project has worked over the past 12 months to specify MyST in the [myst-spec](https://github.com/executablebooks/myst-spec) and an **MEP** process will provide further certainty around how the syntax will evolve.

Once the *MyST Enhancement Process (MEP)* is up and running we will update the community through another blog post. 


## Acknowledgements

This work could not have been done without the support of the [Alfred P. Sloan Foundation](https://sloan.org). 

Many thanks to the Executable Books organisation members including [Aakash Choudhury](https://github.com/AakashGfude), [Chris Holdgraf](https://github.com/choldgraf), [Chris Sewell](https://github.com/chrisjsewell), [Damian Avila](https://github.com/damianavila), [djungelorm](https://github.com/djungelorm), [Fernando Perez](https://github.com/fperez), [Franklin Koch](https://github.com/fwkoch), [Gaige B Paulsen](https://github.com/gaige), [Jonathan Stoppani](https://github.com/GaretJax), [Greg Caporaso](https://github.com/gregcaporaso), [Taneli Hukkinen](https://github.com/hukkin), [John Stachurski](https://github.com/jstac), [Min RK](https://github.com/minrk), [Matt McKay](https://github.com/mmcky), [Yuna Luzi](https://github.com/najuzilu), [Pradyun Gedam](https://github.com/pradyunsg), [Rowan Cockett](https://github.com/rowanc1), [Steve Purves](https://github.com/stevejpurves), [Tomas Beuzen](https://github.com/TomasBeuzen).

We would also like to thank [all collaborators of the project](https://github.com/orgs/executablebooks/outside-collaborators) in addition to [all contributors to the project]().
