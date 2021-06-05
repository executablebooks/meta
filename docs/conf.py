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
copyright = "2020, Executable Book Project"
author = "Executable Book Project"

master_doc = "index"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["myst_nb", "sphinx_panels", "ablog"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

fontawesome_included = True
blog_path = "updates"
blog_title = "Executable Books Updates"
blog_baseurl = "https://executablebooks.org"
blog_feed_archives = True

# Jupyter Notebooks configuration
jupyter_execute_notebooks = "force"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# MyST Configuration
myst_enable_extensions = ["colon_fence"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/logo-wide.png"
html_favicon = "_static/logo-square.png"
html_title = "The Executable Book Project"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Custom scripts ----------------------------------------------------------

import os
from pathlib import Path
import random
import requests
from subprocess import run
from textwrap import dedent
from urllib.parse import urlparse
from ghapi.all import GhApi
import pandas as pd

import yaml

from sphinx.application import Sphinx
from sphinx.util import logging

LOGGER = logging.getLogger("conf")


def update_team(app: Sphinx):
    """Update the directive we use to build the team page with latest results."""
    if os.environ.get("SKIP_TEAM", "").lower() == "true":
        LOGGER.info("Skipping team page...")
        return
    # Pull latest team from github
    LOGGER.info("Updating team page...")
    team_url = "https://api.github.com/orgs/executablebooks/members"
    team = requests.get(team_url).json()

    # Generate the markdown for each member
    people = []
    for person in team:
        this_person = f"""
        ![avatar]({person['avatar_url']})
        ++++++++++++++
        [@{person['login']}]({person['html_url']})
        """
        people.append(this_person)
    people_md = dedent("---\n".join(people))

    # Use the panels directive to build our team and write to txt
    md = f"""
````{{panels}}
---
column: col-lg-4 col-md-4 col-sm-6 col-xs-12 p-2
card: text-center
---

{people_md}
````
    """
    (Path(app.srcdir) / "team_panels_code.txt").write_text(md)


def update_contributing(app: Sphinx):
    if os.environ.get("SKIP_CONTRIBUTE", "").lower() == "true":
        LOGGER.info("Skipping contributing page...")
        return
    LOGGER.info("Updating contributing page...")
    # Grab the latest contributing docs
    url_contributing = "https://raw.githubusercontent.com/executablebooks/.github/master/CONTRIBUTING.md"
    resp = requests.get(url_contributing, allow_redirects=True)
    (Path(app.srcdir) / "contributing.md").write_bytes(resp.content)


def build_gallery(app: Sphinx):
    # Build the gallery file
    LOGGER.info("building gallery...")
    panels_body = []
    projects = yaml.safe_load((Path(app.srcdir) / "gallery.yml").read_text())
    random.shuffle(projects)
    for item in projects:
        if not item.get("image"):
            item["image"] = "https://jupyterbook.org/_static/logo.png"

        repo_text = ""
        star_text = ""

        if item["repository"]:
            repo_text = f'{{link-badge}}`{item["repository"]},"repo",cls=badge-secondary text-white float-left p-2 mr-1,tooltip={item["name"].replace(",", "")}`'

            try:
                url = urlparse(item["repository"])
                if url.netloc == "github.com":
                    _, org, repo = url.path.rstrip("/").split("/")
                    star_text = f"[![GitHub Repo stars](https://img.shields.io/github/stars/{org}/{repo}?style=social)]({item['repository']})"
            except Exception as error:
                pass

        panels_body.append(
            f"""\
        ---
        :img-top: {item["image"]}

        +++
        **{item["name"]}**

        {{link-badge}}`{item["website"]},"website",cls=badge-secondary text-white float-left p-2 mr-1,tooltip={item["name"].replace(",", "")}`
        {repo_text}
        {star_text}
        """
        )
    panels_body = "\n".join(panels_body)

    panels = f"""
````{{panels}}
:container: full-width
:column: text-center col-6 col-lg-4
:card: +my-2
:img-top-cls: w-75 m-auto p-2
:body: d-none

{dedent(panels_body)}
````
    """
    (Path(app.srcdir) / "gallery.txt").write_text(panels)


def update_feature_votes(app: Sphinx):
    # Only create a new file if none exists (so this will only run if you delete the output file)
    path_output = Path(app.srcdir).joinpath("issue-votes.txt")
    if path_output.exists():
        LOGGER.info(f"Found existing feature votes markdown, to re-download, delete {path_output} first.\n")
        return

    # Pull latest issues data
    # If `None`, ghapi will default to GITHUB_TOKEN
    api = GhApi(token=None)
    repos = api.repos.list_for_org("executablebooks")
    issues = []
    LOGGER.info("Retrieving feature voting issue data...")
    for repo in repos:
        for kind in ["enhancement", "type/enhancement", "type/documentation"]:
            issues += api.issues.list_for_repo("executablebooks", repo['name'], labels=kind, per_page=100, state="open")

    # Extract the metadata that we want
    df = pd.DataFrame(issues)
    df['👍'] = df['reactions'].map(lambda a: a['+1'])
    df['Repository'] = df['html_url'].map(lambda a: f"[{a.rsplit('/')[4]}]({a.rsplit('/', 2)[0]})")
    df['Author'] = df['user'].map(lambda a: f"[@{a['login']}](https://github.com/{a['login']})")
    df['Issue'] = df['html_url'].map(lambda a: f"[#{a.rsplit('/')[-1]}]({a})")
    df = df.rename(columns={"title": "Title"})

    # Sort and remove issues with a very small # of votes
    df = df.sort_values("👍", ascending=False)
    df = df[df['👍'] > 1]

    # Write to markdown
    LOGGER.info("Writing feature voting issues to markdown...")
    df[['👍', 'Repository', "Issue", 'Title', 'Author']].to_markdown(path_output, index=False)


def setup(app: Sphinx):
    app.add_css_file("custom.css")
    app.connect("builder-inited", update_team)
    app.connect("builder-inited", update_contributing)
    app.connect("builder-inited", build_gallery)
    app.connect("builder-inited", update_feature_votes)
