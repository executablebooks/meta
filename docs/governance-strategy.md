# A bootstrap decision-making process and source of truth for Executable Books

:::{note}

This is a proposal for bootstrapping a formal decision-making and team policy process.
It proposes a new location for organizational policy - a `team-compass`, but since this space does not currently exist, I am making this "proposal" by adding it as a PR to the `meta/` repository, which is currently our home for organizational policy. If accepted, I will remove this page and migrate content over to `compass.executablebooks.org`.

:::

Below is a bootstrap plan for encoding the Executable Books team policy and decision-making process. Its goal is to be as simple as possible and not deviate too much from our current practices (to maximize the chances of being followed). It also aims to balance "formal process" against "efficient asynchronous decision-making" (to avoid being so slow that it hinders the organization).

Over time, as we learn what works and what doesn't, we may make amendments to this process to make it more complex.

:::{admonition} Acknowledgements
This builds off of the work that Chris Sewell did in creating the current [MyST Enhancement Proposals repository](https://myst-eps.readthedocs.io/en/latest/mep-0001.html). It takes much of the process there, and tries to simplify and slim it down. It also separates out two different processes - a more complex one for MyST, and a simpler one for organizational policy. We can revisit this in the future if we believe that we _need_ more complexity in one or the other. Many thanks to Chris S (and others) for feedback and inspiration for these ideas.
:::

## Groups with decision-making power in the Executable Books organization

### Steering Council

The group of people with decision-making authority over the entire organization. Their primary duty is to set organizational policy and strategy, to steward all technical and IP assets of the organization, to make decisions when we are at an impasse, and to delegate decision-making power to others in the organization. Members of the steering council all have "owner" status of the [executablebooks](https://github.com/executablebooks) GitHub organizations and repositories, and are the only individuals with "owner" status.

The Steering Council is currently comprised of the three Principle Investigators of the original grant funding the project: [Chris Holdgraf](https://github.com/choldgraf), [John Stachurski](https://github.com/jstac), and [Greg Caporaso](https://github.com/gregcaporaso). We expect the Steering Council to expand in the future, and this initial Steering Council will define policies that set the expectations for steering council membership as well as the process for modifying or expanding the steering council membership in the future.

### Core team members

Individuals who are particularly interested in the EBP community and have demonstrated a willingness to participate in our community and further its mission. They guide discussion, grow the community, contribute code, and generally help the project improve.

Currently the core team is [defined here](https://executablebooks.org/en/latest/team.html).

## Three sources of truth

### `executablebooks/team-compass`: Team Policy

Our Team Compass is the Source of Truth (SoT) for all organizational policy[^1]. The Team Compass should make it clear what is _policy_ and what is _guidance_. It should define clear sections that are community "musts" and others that are "guidelines and recommendations".

It can also delegate SoT status to other places in the organization. It delegates the SoT for the MyST specification to `myst-spec/`.

[^1]: A Team Compass is common in the Jupyter ecoystem (e.g., [here is JupyterHub's Team Compass](https://jupyterhub-team-compass.readthedocs.io/en/latest/index-team_guides.html). In fact, Jupyter's governance model will soon [require that sub-projects have their own Team Compass](https://jupyter.org/governance/software_subprojects.html?responsibilities-of-jupyter-subprojects)

#### How to change team policy

Take the following steps for changing any policy, strategy, or governance aspects of the Team Compass.

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
   - If all steering council members `Approve`, it may be merged any time.


[^blocking]: When blocking any change or objecting to a proposal, provide a rationale for what must be changed and why you believe it is critically important. _Do not disapprove because of differences in opinion. Only disapprove if you have a major strategic concern_. See [Strategies for integrating objections](https://www.sociocracyforall.org/strategies-for-integrating-objections/) for what we are aiming for.


### `executablebooks/myst-spec`: The MyST Specification

`executablebooks/myst-spec` is the Source of Truth for the MyST Specification. It uses a combination of documentation, examples, schemas, tests, etc to define MyST markdown in a form that others could use to implement parsers and renderers. It is versioned and includes "releases" in order to make it easy for downstream implementors to track the changes they need to make.

```{admonition} Implementation detail
This repository will need to be modified as-needed to be the source of truth for the MyST Specification, and to have enough information to teach newcomers about its structure and function. One example for inspiration: [the Zarr specifications page](https://zarr.readthedocs.io/en/stable/spec.html).
```

The MyST Specification is changed through the MyST Enhancement Proposal process, described below.

### `executablebooks/myst-eps`: MyST Enhancement proposals

Because the MyST specification has many interior and exterior stakeholders, we use a more formal and structured process around changing the specification. This process is encoded in `executablebooks/myst-eps` and described briefly below

1. **Open an issue in `myst-eps`** that describes the enhancement you'd like to make. The goal of the issue is to help others understand your idea and get informal alignment around it. _MEPs should ideally have at least two, and ideally 3-4 co-authors from different organizations._
2. **Make a proposal via a PR to `myst-eps`**. Use a markdown template to structure your proposal. The `status` should initially be set to `Draft`. Here's a proposed template:
   
   ```
   ---
   mep:
      id: <NNNN - increment last active MEP # by 1>
      created: <yyyy-mm-dd - date MEP is active>
      authors:
        - <authors' real names, optional github handle>
      status: <Draft | Active | Accepted | Not Accepted>
      discussion: <URL of canonical location for discussion>
   ---
   # <title here>

   ## Context
   
   <!-- provide context needed to understand this proposal. Describe the problem with MyST's current syntax or behavior. -->
   
   ## Proposal
   
   <!-- describe your proposed change to syntax in concrete terms. Include a layperson's description of this change if relevant. -->
   
   ## Examples
   
   <!-- provide examples of what this change would look like in the real world (e.g., raw MyST and rendered output). -->
   
   ## UX implications
   
   <!-- describe how this would improve the UX or functionality of MyST markdown. Describe any deprecations or syntax migration steps that would be needed. -->
   
   ## Questions or objections
   
   <!-- as conversation takes place, list anything that is needed to be resolved and provide links to the conversation where this happened. -->
   
   ## References
   
   <!-- reference other examples you're using for inspiration or to help others learn and understand the proposal. -->
   ```
3. **Iterate on proposal**. Actively invite discussion from others in the community. As individuals (particularly core team members) raise objections or make suggestions, incorporate their ideas as changes into the proposal.
4. **Make a decision**. Once the proposal has stabilized and the author wishes to move forward, make a commit to the PR to set the status as `Active`.
   - The MEP should no-longer change substantially and **the Core Team** should review and approve if they wish.
   - To approve, then `Approve` the Pull Request in the GitHub UI.
   - To request blocking changes, then `Request Changes` in the GitHub UI.[^blocking]
   - A MEP may be accepted when:
     - More than 2 working days have passed since the proposal was marked as `Active`.
     - At least two `PR Approvals` from **core team members**.
     - No `Request Changes` from a core team member.
  - If the MEP is accepted, update its status metadata to `Accepted` and merge the PR. Once a PR is merged, it closes the issue and a decision has been made.
  - The changes in the MEP then become "part of the myst spec" via a Pull Request to `myst-spec` that anyone is welcome to implement.
  - If there are unresolved objections (via `Request Changes` to the PR), then the MEP author may restart the voting process after incorporating feedback to resolve the objection, or ask the Steering Council to decide following the same decision-making process used in `meta/`.
