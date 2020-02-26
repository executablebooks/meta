# The Executable Book Project

This is the public-facing site for the ExecutableBookProject, an international
collaboration to build open source tools that make it easier to publish
computational narratives with the Jupyter ecosystem.

## The EBP's technical goal

The goal of the EBP is to build tools that make it easier to create
professoinal computational narratives using open source tools, and utilizing
a purely open-source stack. We would like users in the scientific, academic,
and data science communities to be able to do the following:

* **Write their content in either markdown text files, or Jupyter Notebooks**.
  These files should have rich content - outputs from running code, references
  and cross-references, equations, etc.
* **Execute content and cache the results**. Notebooks that did not change any
  code cells should not be re-run. Those that *did* change code cells should
  have their cells re-executed, and the results stored in a robust cache.
* **Combine cached outputs with content files with a document model**. Using
  the excellent Sphinx documentation stack, documents can include many features
  for publishing, such as equations, cross-references, and citations.
* **Build interactive HTML or publication-quality PDF outputs**. Sometimes
  users wish to create rich and interactive websites, other times they want to
  send a high-quality PDF to a publisher. This system should treat both as
  equal citizens.
* **Control everything above with a simple command-line interface**. Most
  users should not have to know anything about Sphinx, cacheing, etc. A simple
  CLI should control most of the complexity of this process.

## Our principles and constraints

In running this project, we aim to adhere to several principles that we believe
will result in higher-quality technology that aligns with the core principles
of the open source community. Here are a few key components:

* **Support casual users equally to power users**. Complicating the feature
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
  of Sphinx, Latex, etc should not be a requirement. They should only need to
  use a simple tool to control the process.
* **Don't try to do everything**. Focus our tools on publishing
  computational documents with reasonable choices made for the user.

Browse the rest of this site for more information about what we're working
on and our plans for what's coming next.

```{toctree}
about.md
tools.md
updates/index.md
examples.md
```
