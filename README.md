# Executable Books Meta Project

This is a repository for team planning, coordination, and discussion that doesn't belong in any specific code repository.

It also serves as documentation about the Executable Books Project itself.

## Build the documentation

To build the documentation the easiest thing to do is to use `tox`.
This will automatically install the environment needed for the documentation each time you build it.

Install `tox` with:

```
pip install tox
```

then navigate to `meta/` and run the following:

```
tox -e docs-update
```

this will install the necessary environment the first time, then build the documentation for you.

**To use a live documentation preview** you may run the following command:

```
tox -e docs-live
```

Note that this documentation uses the GitHub API to pull data about issue voting.
To use it, you should [generate a personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) and then assign it to the environment variable `GITHUB_TOKEN`.
