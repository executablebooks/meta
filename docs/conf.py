# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

# -- Project information -----------------------------------------------------

project = "Executable Book Project"
copyright = "2024, Executable Book Project"
author = "Executable Book Project"

root_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_nb", "sphinx_design", "ablog", "sphinx.ext.intersphinx", "sphinxext.opengraph", "sphinxext.rediraffe"]

fontawesome_included = True
blog_path = "blog"
blog_title = "Executable Books Blog"
blog_baseurl = "https://executablebooks.org"
blog_feed_archives = True

# Jupyter Notebooks configuration
nb_execution_mode = "force"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# MyST Configuration
myst_enable_extensions = ["colon_fence", "linkify", "substitution", "deflist"]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/logo-wide.svg"
html_favicon = "_static/logo-square.png"
html_title = ""

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "repository_url": "https://github.com/executablebooks/meta",
    "repository_branch": "main",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_edit_page_button": True,
    "path_to_docs": "docs",
}

# Intersphinx
intersphinx_mapping = {"jb": ("https://jupyterbook.org/en/latest", None), "tc": ("https://compass.executablebooks.org/en/latest/", None)}

# Opengraph social cards
ogp_social_cards = {
    "image": "_static/logo-square.png",
}
ogp_site_url = "https://executablebooks.org/en/latest/"

# Redirections
rediraffe_redirects = {
    "blog/2023/announce-mystjs.md": "blog/2023-02-09-announce-mystjs.md",
}

# -- Custom scripts ----------------------------------------------------------
import itertools
import os
from pathlib import Path
import random
import requests
from subprocess import run
from textwrap import dedent
from urllib.parse import urlparse
from ghapi.all import GhApi, paged
import pandas as pd

import yaml

from sphinx.application import Sphinx
from sphinx.util import logging

LOGGER = logging.getLogger("conf")

def build_gallery(app: Sphinx):
    # Build the gallery file
    LOGGER.info("building gallery...")
    grid_items = []
    projects = yaml.safe_load((Path(app.srcdir) / "gallery.yml").read_text())
    random.shuffle(projects)
    for item in projects:
        if not item.get("image"):
            item["image"] = "https://jupyterbook.org/_images/logo-square.svg"

        repo_text = ""
        star_text = ""

        if item["repository"]:
            repo_text = f'{{bdg-link-secondary}}`repo <{item["repository"]}>`'

            try:
                url = urlparse(item["repository"])
                if url.netloc == "github.com":
                    _, org, repo = url.path.rstrip("/").split("/")
                    star_text = f"[![GitHub Repo stars](https://img.shields.io/github/stars/{org}/{repo}?style=social)]({item['repository']})"
            except Exception as error:
                pass

        grid_items.append(
            f"""\
        `````{{grid-item-card}} {" ".join(item["name"].split())}
        :text-align: center

        <img src="{item["image"]}" alt="logo" loading="lazy" style="max-width: 100%; max-height: 200px; margin-top: 1rem;" />

        +++
        ````{{grid}} 2 2 2 2
        :margin: 0 0 0 0
        :padding: 0 0 0 0
        :gutter: 1

        ```{{grid-item}}
        :child-direction: row
        :child-align: start
        :class: sd-fs-5

        {{bdg-link-secondary}}`website <{item["website"]}>`
        {repo_text}
        ```
        ```{{grid-item}}
        :child-direction: row
        :child-align: end

        {star_text}
        ```
        ````
        `````
        """
        )
    grid_items = "\n".join(grid_items)

# :column: text-center col-6 col-lg-4
# :card: +my-2
# :img-top-cls: w-75 m-auto p-2
# :body: d-none

    panels = f"""
``````{{grid}} 1 2 3 3
:gutter: 1 1 2 2

{dedent(grid_items)}
``````
    """
    (Path(app.srcdir) / "gallery.txt").write_text(panels)


def update_feature_votes(app: Sphinx):
    """Update the +1 votes for features.

    This will only run if `issue-votes.txt` does not exist and if a GITHUB_TOKEN
    environment variable is present.
    """
    # Only create a new file if none exists (so this will only run if you delete the output file)
    path_output = Path(app.srcdir).joinpath("issue-votes.txt")
    if path_output.exists():
        LOGGER.info(
            f"Found existing feature votes markdown, to re-download, delete {path_output} first.\n"
        )
        return

    # Pull latest issues data
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        LOGGER.info(
            f"No token found at {os.environ.get('GITHUB_TOKEN')}, GitHub "
            "issue information will not be used. "
            "Create a GitHub Personal Access Token and assign it to GITHUB_TOKEN"
        )
        return
    api = GhApi(token=token)
    repos = api.repos.list_for_org("executablebooks")
    issues = []
    LOGGER.info("Retrieving feature voting issue data...")
    for repo in repos:
        for kind in ["enhancement", "type/enhancement", "type/documentation"]:
            issues.extend(
                itertools.chain.from_iterable(
                    paged(api.issues.list_for_repo,
                        owner="executablebooks", repo=repo["name"], labels=kind, state="open"
                    )
                )
            )

    # Extract the metadata that we want
    df = pd.DataFrame(issues)
    df["👍"] = df["reactions"].map(lambda a: a["+1"])
    df["Repository"] = df["html_url"].map(
        lambda a: f"[{a.rsplit('/')[4]}]({a.rsplit('/', 2)[0]})"
    )
    df["Author"] = df["user"].map(
        lambda a: f"[@{a['login']}](https://github.com/{a['login']})"
    )
    df["Issue"] = df["html_url"].map(lambda a: f"[#{a.rsplit('/')[-1]}]({a})")
    df = df.rename(columns={"title": "Title"})

    # Sort and remove issues with a very small # of votes
    df = df.sort_values("👍", ascending=False)
    df = df[df["👍"] > 1]

    # Write to markdown
    LOGGER.info("Writing feature voting issues to markdown...")
    df[["👍", "Repository", "Issue", "Title", "Author"]].to_markdown(
        path_output, index=False
    )


def setup(app: Sphinx):
    app.add_css_file("custom.css")
    app.connect("builder-inited", build_gallery)
    app.connect("builder-inited", update_feature_votes)
