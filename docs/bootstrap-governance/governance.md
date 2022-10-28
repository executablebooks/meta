# Governance of Executable Books

```{note}
_All contributors_ to the Executable Books Project (including but not limited to individuals contributing code, providing technical support, teaching workshops, and engaging in discussions about changes to EBP policy or the MyST Specification) are expected to adhere to the [Code of Conduct](policy:coc).
```

This page describes the groups of people with decision-making authority in the project, as well as the Sources of Truth for organizational policy and the process around changing it.

## Decision-making groups

### Steering Council

Have decision-making authority over the entire organization.
Their primary duty is to set organizational policy and strategy, to steward all technical and IP assets of the organization, to make decisions when we are at an impasse, and to delegate decision-making power to others in the organization. 

The Steering Council is currently comprised of the three Principal Investigators of the original grant funding the project: [Chris Holdgraf](https://github.com/choldgraf), [John Stachurski](https://github.com/jstac), and [Greg Caporaso](https://github.com/gregcaporaso).

```{note}
We expect the Steering Council to expand in the future, and this initial Steering Council will define policies that set the expectations for steering council membership as well as the process for modifying or expanding the steering council membership in the future.
```

#### Responsibilies

```{note}
This is intentionally blank for now, we will add more information in the coming weeks.
```

% - Define organizational policy, strategy, and values
% - Hold the community accountable to its mission and its code of conduct
% - Oversee the structure and system of work in the community
% - Delegate authority and responsibility to position the project for success

#### Expectations

```{note}
This is intentionally simple for now, we will add more information in the coming weeks.
```

Steering Council Members agree to abide by the [EBP Code of Conduct](policy:coc).


#### Privileges

- _Owner_ status of the [executablebooks](https://github.com/executablebooks) GitHub organizations and repositories.
- Access to any credentials or accounts that the project uses. At least two Steering Council members must have access to all project credentials.
- All [Core Team privileges](governance:privileges:core-team)=

### Core team members

Individuals who are particularly interested in the EBP community and have demonstrated a willingness to participate in our community and further its mission. They guide discussion, grow the community, contribute code, and generally help the project improve.

Currently the core team is [defined here](https://executablebooks.org/en/latest/team.html).

#### Responsibilities

```{note}
This is intentionally blank for now, we will add more information in the coming weeks.
```


#### Expectations

```{note}
This is intentionally simple for now, we will add more information in the coming weeks.
```

Core Team Members agree to abide by the [EBP Code of Conduct](https://github.com/executablebooks/.github/blob/master/CODE_OF_CONDUCT.md).

(governance:privileges:core-team)=
#### Privileges

```{note}
This is intentionally simple for now, we will add more information in the coming weeks.
```

- Write permissions for any repository they are willing to steward.
- Voting privileges for [MyST Enhancement Proposals](governance:meps).

## Sources of truth

### Team Policy

Team Policy is defined at the [`executablebooks/team-compass`](https://github.com/executablebooks/team-compass) repository. 

Our Team Compass is the Source of Truth (SoT) for all organizational policy[^1]. The Team Compass should make it clear what is _policy_ and what is _guidance_. It should define clear sections that are community "musts" and others that are "guidelines and recommendations".

It can also delegate SoT status to other places in the organization. It delegates the SoT for the MyST specification to `myst-spec/`.

[^1]: A Team Compass is common in the Jupyter ecoystem (e.g., [here is JupyterHub's Team Compass](https://jupyterhub-team-compass.readthedocs.io/en/latest/index-team_guides.html). In fact, Jupyter's governance model will soon [require that sub-projects have their own Team Compass](https://jupyter.org/governance/software_subprojects.html?responsibilities-of-jupyter-subprojects)

(governance:policy-decision)=
#### How to change team policy

Take the following steps for changing any policy, strategy, or governance aspect of the Team Compass.

1. **Open an issue** to explain the policy that you'd like to change, and why. Here is a rough template to follow:
   ```
   ## Context
   
   provide context needed to understand this proposal. Describe the problem this proposal will solve.
   
   ## Proposal
   
   describe your proposal in informal but specific terms.
   
   ## Impact
   
   describe the implications of this proposal and the impact it will have.
   ```
2. **Discuss and incorporate feedback** with others on the team. If there are objections or suggestions, do your best to incorporate them into your proposal.
3. **Make a Pull Request** to the `Team Compass` repository (or another location if appropriate) and link it to the issue. This is the "formal change" that you wish to make.
4. **Make a decision**. Steering Council members may approve PRs to change policy. To approve a change, use the "Approve" feature in the GitHub UI. To request blocking changes, use the "Request Changes" feature in the GitHub UI[^blocking]. PRs to change organizational policy may be merged when the following conditions are met:
   - Have been open for five working days
   - Have `Approval` from at least **One  Steering Council member**
   - Have no `Request Changes` from a Steering Council member.
   - If there are unresolveable objections from a Steering Council member, a decision to merge is made with a majority vote.
   - If all steering council members `Approve`, it may be merged any time, overriding the requirement of being open for five working days.


[^blocking]: When blocking any change or objecting to a proposal, provide a rationale for what must be changed and why you believe it is critically important. _Do not disapprove because of differences in opinion. Only disapprove if you have a major strategic concern_. See [Strategies for integrating objections](https://www.sociocracyforall.org/strategies-for-integrating-objections/) for what we are aiming for.


### The MyST Specification

The MyST Specification is defined at [`executablebooks/myst-spec`](https://github.com/executablebooks/myst-spec). The process for changing it is defined at [`executablebooks/myst-enhancement-proposals`](https://github.com/executablebooks/myst-enhancement-proposals).

`executablebooks/myst-spec` is the Source of Truth for the MyST Specification. It uses a combination of documentation, examples, schemas, tests, etc to define MyST markdown in a form that others could use to implement parsers and renderers. It is versioned and includes "releases" in order to make it easy for downstream implementors to track the changes they need to make.

```{admonition} Implementation detail
This repository will need to be modified as-needed to be the source of truth for the MyST Specification, and to have enough information to teach newcomers about its structure and function. One example for inspiration: [the Zarr specifications page](https://zarr.readthedocs.io/en/stable/spec.html). [Here's a comment with some suggestions for what is missing](https://github.com/executablebooks/meta/pull/843#issuecomment-1275474229).
```

The MyST Specification is changed through the MyST Enhancement Proposal process, described below.

#### How to change the MyST specification: MyST Enhancement Proposals

See [](meps.md).
