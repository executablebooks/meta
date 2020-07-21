# The Executable Book Project

This is the public-facing site for
[ExecutableBookProject](https://github.com/executablebooks), an international
collaboration to build open source tools that facilitate publishing
computational narratives using the Jupyter ecosystem.

## The EBP's technical goals

The goal of the EBP is to build tools that facilitate creating
professional computational narratives (books, lecture series, articles, etc.) 
using open source tools. We want users in the scientific, academic,
and data science communities to be able to do the following:

* **Write their content in either markdown text files, or Jupyter Notebooks**.
  These files include rich content - outputs from running code, references
  and cross-references, equations, etc.
* **Execute content and cache the results**. Intelligent caching means
  that only modified code cells are re-run. 
* **Combine cached outputs with content files with a document model**. Using
  the excellent [Sphinx](https://www.sphinx-doc.org/en/master/) documentation
  stack, documents can include many features for publishing, such as
  equations, cross-references, and citations.
* **Build interactive HTML or publication-quality PDF outputs**. Sometimes
  users wish to create rich and interactive websites, other times they want to
  send a high-quality PDF to a publisher. This system will treat both as
  equal citizens.
* **Control everything above with a simple command-line interface**. Most
  users should not have to know anything about Sphinx, caching, etc. A simple
  user interface will hide most of the complexity of this process.

See the [tools section](tools) for a few examples of the tools we've created
as a part of this project.

## Our principles and constraints

In running this project, we aim to adhere to several principles that we believe
will result in higher-quality technology that aligns with the core principles
of the open source community. Here are a few key components:

* **Give equal support to casual users and power users**. Complicating the feature
  space to support a "power user feature" should be done with great care.
* **Build modular components that are useful elsewhere**. Rather than building
  a single vertical stack, find parts of the workflow that naturally separate.
  Create modular tools for these parts so that they may benefit the community
  outside of the context of building interactive books.
* **Use pre-existing technology where possible**. Rather than re-inventing
  the wheel, make every effort to utilize pre-existing open source tech.
* **Use pre-existing standards where possible**. In the event that we must
  create new patterns of content creation or tooling, utilize prior art in
  the open source community as much as possible, especially when it comes to
  markup languages.
* **Contribute improvements upstream**. Where we utilize pre-existing tools,
  contribute improvements to them as we build off of them for this project.
* **Design for the future**. While we have a bit of funding now, it won't last
  forever. This means the technology should be easy for potential developers
  to read, understand, and modify/improve.
* **Users should not need to know anything about the build system**. If they
  want to dig into the guts of our infrastructure, they can, but knowledge
  of Sphinx, Latex, and so on should not be a requirement. They should only need to
  use a simple tool to control the process.
* **Don't try to do everything**. Focus our tools on publishing
  computational documents with reasonable choices made for the user.

Browse the rest of this site for more information about what we're working
on and our plans for what's coming next.

```{toctree}
about.md
tools.md
team.md
updates/index.md
dev-conventions.md
examples.md
```
