# 🚀 RELEASE: Jupyter Book v0.11.1

```{post} 2021-06-05
---
author: EBP
image: 1
excerpt: 2
---
```

```{note}
This is an experimental post to try solving two problems with one blog post.
We often send out a flurry of tweets to talk about a new release in the Executable Books stack.
We'd also like to blog about releases more often so it's easier to track major updates.
This post is an attempt at crafting a blog post entirely made out of tweets!
```

We're pleased to announce a new version of Jupyter Book has just been released! You can check out the CHANGELOG here: https://jupyterbook.org/reference/_changelog.html#v0-11-0

⚠BREAKING CHANGE⚠.
The Table of Contents structure is now slightly different. It now follows a "schema" that makes the TOC easier to parse and understand. See the changelog for details: https://jupyterbook.org/reference/_changelog.html#breaking

In addition, there are a few nice command line options for *migrating* an old TOC to a new one, as well as creating TOCs from book structures, and vice versa. For example: https://jupyterbook.org/structure/toc-generate.html

As a result, we are also now using an external dependency to handle our Table of Contents - sphinx-external-toc, which you may use on your own with Sphinx as well: https://sphinx-external-toc.readthedocs.io/en/latest/intro.html

Finally, we've also got a nifty new logo refresh, as well as a square logo!
Check them out below:

```{figure} https://github.com/executablebooks/jupyter-book/blob/master/docs/images/logo-wide.svg?raw=true
ooooh
```

```{figure} https://github.com/executablebooks/jupyter-book/blob/master/docs/images/logo-square.svg?raw=true
---
width: 100
---
aaah
```

Many thanks to everybody in the Executable Books community for helping make this release happen! And thanks to Sloan Foundation for supporting development of this release ✨
