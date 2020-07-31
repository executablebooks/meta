#!/usr/bin/env python
"""Create issues JSON"""

import json
import os
import requests
import sys

# The GraphQL query
QUERY_TEMPLATE = """
query {{
  repository(owner: "{org_name}", name: "{repo_name}") {{
    name
    issues(first: 100 {after}, states:OPEN, labels:["{label}"], orderBy: {{field: CREATED_AT, direction: ASC}}) {{
      edges {{
        node {{
          number
          url
          title
          author{{login, url}}
          reactions(content: THUMBS_UP) {{
            totalCount
          }}
          bodyHTML
        }}
      }}
      pageInfo {{
        endCursor
        hasNextPage
      }}
    }}
  }}
}}
"""


def run_query(query: str, token: str = None):
    """See https://docs.github.com/en/graphql/guides/forming-calls-with-graphql#authenticating-with-graphql"""
    headers = {
        "Authorization": f"Bearer {token or os.environ['GITHUB_AUTH_TOKEN']}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    request = requests.post(
        "https://api.github.com/graphql", json={"query": query}, headers=headers
    )
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception(
            "Query failed to run by returning code of {}. {}".format(
                request.status_code, query
            )
        )


def fetch_issue_chunk(cursor, repo_name, org_name, label, token=None):
    """Get chunk of up to 100 issues (max for each request)."""
    query = QUERY_TEMPLATE.format(
        org_name=org_name,
        repo_name=repo_name,
        label=label,
        after=f', after: "{cursor}"' if cursor else "",
    )
    data = run_query(query, token)["data"]["repository"]["issues"]

    return {
        "issues": [
            {
                "repo": repo_name,
                "title": i["node"]["title"],
                "number": i["node"]["number"],
                "url": i["node"]["url"],
                "author_url": i["node"]["author"]["url"],
                "author_name": i["node"]["author"]["login"],
                "body": i["node"]["bodyHTML"],
                "votes": i["node"]["reactions"]["totalCount"],
            }
            for i in data["edges"]
        ],
        "hasNextPage": data["pageInfo"]["hasNextPage"],
        "endCursor": data["pageInfo"]["endCursor"],
    }


def fetch_issues(
    repo_name, org_name="executablebooks", label="enhancement", token=None
):
    issues = []
    more_pages = True
    requests_num = 0  # avoid infinite loops
    cursor = None

    while more_pages and requests_num < 99:

        data = fetch_issue_chunk(cursor, repo_name, org_name, label, token)
        issues.extend(data["issues"])
        cursor = data["endCursor"]
        more_pages = data["hasNextPage"]
        requests_num += 1

    return issues


def create_issues_json(path):

    issues = []
    for repo_name in ["jupyter-book", "MyST-Parser", "MyST-NB", "markdown-it-py"]:
        print("fetching:", repo_name)
        issues.extend(fetch_issues(repo_name))

    issues = sorted(issues, key=lambda i: i["votes"], reverse=True)

    with open(path, "w") as handle:
        json.dump(issues, handle)


if __name__ == "__main__":
    create_issues_json(sys.argv[1] if len(sys.argv) > 1 else "issues.json")
