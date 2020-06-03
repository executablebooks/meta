"""Update the directive we use to build the team page with latest results."""
from requests import get
from IPython.display import Markdown
from pathlib import Path
from textwrap import dedent

# Pull latest team from github
print("Updating team page...")
team_url = "https://api.github.com/orgs/executablebooks/members"
team = get(team_url).json()

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
Path("team_panels_code.txt").write_text(md)


