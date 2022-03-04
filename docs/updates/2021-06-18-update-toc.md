# Migrate your old Table of Contents to the new TOC structure

```{post} 2021-06-17
---
author: EBP
image: 1
excerpt: 2
---
```

In Jupyter Book v0.11, we [introduced a new Table of Contents](https://jupyterbook.org/reference/_changelog.html#v0-11-0) structure.
The new structure is a bit more rigid and explicit, which should allow for a cleaner mapping of TOC structures onto book structures.
It also introduces the concept of TOC **formats**, which allows you to specify different _kinds_ of documents in the TOC (to start with, Books and Articles).

This is a short guide to explain the differences between the old and new Table of Contents structures, to help you update them.

:::\{seealso}
If you'd like to automatically convert your Table of Contents, you may also try running the following command:

```bash
jupyter-book toc migrate path/to/_toc.yml
```

This will automatically generate a new TOC, though it will remove comments and may slightly alter formatting.
:::

## Step 0: Starting with an old Table of Contents structure

Let's say you're starting with this Table of Contents structure:

```yaml
- file: intro
  numbered: true
- part: Get started
  chapters:
  - file: start/overview
  - file: start/build
  - file: start/publish
    sections:
      - file: publish/gh-pages
      - file: publish/netlify
```

This structure defines a landing page from the file `intro`, as well as a single part with a few chapters inside.

Next we'll convert this to the new TOC format.

## Step 1: define a "root" page

The new TOC format requires an explicit page to be set as your document's "root".
This is the first page that users see when they navigate your book or article.
To add one, we'll explicitly define our `intro` page as the root document and move it to the root of the YAML file.

```yaml
root: intro
numbered: true
- part: Get started
  chapters:
  - file: start/overview
  - file: start/build
  - file: start/publish
    sections:
      - file: publish/gh-pages
      - file: publish/netlify
```

## Step 2: Add a "format" key

The new TOC structure asks you to explicitly define a **format** for the Table of Contents.
This helps Jupyter Book know what kind of document you are building.
You currently have two options:

- `format: jb-book` for multi-page books
- `format: jb-article` for articles made up of sections

Different kinds of documents have different TOC key names.
For example, Books map on to "parts" and "chapters" at a top level, and "sections" underneath each chapter.
Articles may have collections of "sections", but no "parts" and "chapters".

In this case, we have "parts" defined, so we'll choose the `jb-book` format.

```yaml
root: intro
format: jb-book
numbered: true
- part: Get started
  chapters:
  - file: start/overview
  - file: start/build
  - file: start/publish
    sections:
      - file: publish/gh-pages
      - file: publish/netlify
```

## Step 3: Explicitly define the parts

The collection of "parts" now exists underneath a `parts` key.
The value of `parts` is a **list** where each item corresponds to one part.
We now use the `caption` key to define the title of each part.

```yaml
root: intro
format: jb-book
numbered: true
parts:
- caption: Get started
  chapters:
  - file: start/overview
  - file: start/build
  - file: start/publish
    sections:
      - file: publish/gh-pages
      - file: publish/netlify
```

:::\{admonition} An alternative structure for single-part books
If your book only consists of a single part, you could directly add the `chapters` key to the root of your TOC, like so:

```yaml
root: intro
format: jb-book
numbered: true
chapters:
- file: start/overview
- file: start/build
- file: start/publish
  sections:
    - file: publish/gh-pages
    - file: publish/netlify
```

:::

## Step 4: Move the configuration

The new TOC structure has a more explicit configuration structure, and has different locations for global configuration and section configurations.

Because we wish for **all** sections to be numbered, we will keep `numbered: true`, but must move it to a `defaults` key, which makes it a default for all pages in the TOC.

```yaml
root: intro
format: jb-book
defaults:
  numbered: true
parts:
- caption: Get started
  chapters:
  - file: start/overview
  - file: start/build
  - file: start/publish
    sections:
      - file: publish/gh-pages
      - file: publish/netlify
```

## Step 5: We're done!

This TOC structure is now compatible with the new Jupyter Book TOC style.
We have taken a minimal set of steps here to convert over the old TOC structure, but if you'd like to learn more about the Table of Contents, check out {ref}`jb:toc/structure`.
