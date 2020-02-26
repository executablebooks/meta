# Projects

The following is a list of projects that this project will support and develop. The following projects fit together to form the 
Executable Book Project. 

```{contents} Contents:
```

## Overview

{{ add Version 3 build diagram }}

High level feature lists are provided as a simple measure of progress. `Phase 1` are items required for minimal viable product, `Phase 2` include items that are planned for initial release, and 
`Phase 3` captures wishlist items to be implemented in the future.

## Authoring Tools

### [JupyterText](https://github.com/mwouts/jupytext) [External]

**Description:** 

Jupyter Notebooks as Markdown Documents, Julia, Python or R scripts

**Contribution:** 

The primary aim is to add myst to jupytext to enable *bi-directional* conversion 
between IPYNB and myst text based files. 

A seconday objective is to understand how JupyText may be used to convert between 
ipynb and myst files in quasi-realtime to enable joint editing between the 
two formats. 

**Lead:** [Aakash](https://github.com/AakashGfude)

## Parsers

### [myst-parser](https://github.com/ExecutableBookProject/MyST-Parser) [Internal]

**Description:** 

An extended commonmark compliant parser, with bridges to docutils/sphinx

**Lead:** [Chris Sewell](https://github.com/chrisjsewell)

For supported syntax please refer to [here](https://github.com/ExecutableBookProject/MyST-Parser#parsed-token-classes)

### [myst-nb](https://github.com/ExecutableBookProject/MyST-NB) [Internal]

**Description:** Enables sphinx to read IPYNB files that contain
myst based syntax

**Lead:** [Chris Holdgraf](https://github.com/choldgraf)

## Jupyter Notebook Execution

### [jupyter-cache](https://github.com/ExecutableBookProject/jupyter-cache) [Internal]

**Description:** 

Provide caching and execution control for a
collection of Jupyter notebooks.

**Features:**

*Phase 1:*

- [ ] provide cache for a set of notebooks to track changes
- [ ] execute notebooks and save outputs

*Phase II:*

- [ ] parallel execution of notebooks
- [ ] support for notebook file dependencies (i.e. assets such as data files, images)

*Phase III:*

- [ ] support to specify `ipynb` execution ordering and dependency

## Build Tools

### Command Line Tool (jupyterbook)

**Description:**

Enable unified command line tool to coordinate the underlying packages and building targets using `sphinx`