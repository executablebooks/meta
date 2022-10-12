(governance:meps)=
# MyST Enhancement Proposals

Because the MyST specification has many interior and exterior stakeholders, we use a more formal and structured process around changing the specification.
These are called **MyST Enhancement Proposals (MEPs)**.
This process is encoded in `executablebooks/myst-enhancement-proposals` and described briefly below.

## Goals of the MEP process

- **Formal without being oppressive**. Provide slightly more structure than our organizational policy, to account for the fact that MEPs have many more stakeholders and decision-makers. However keep it as simple as possible to avoid overly-complex discussion that leads to frustrating and inefficient decision-making.
- **Make the process inclusive**. Ensure a process for discussion and deciding that is inclusive and that encourages productive discussion from many parts of the project.
- **Make the process efficient**. Ensure that there is enough information, and with the right structure, to have focused asynchronous discussion that leads to a decision-making cadence that is sustainable for the project.
- **Design for many stakeholders**. Ensure that the specification evolves in a way that benefits our major stakeholders, and that is not unintentionally over-fit to the perspective of only a subet of the Executable Books community.

## The MEP process

1. **Open an issue in `myst-enhancement-proposals`** that describes the enhancement you'd like to make. The goal of the issue is to help others understand your idea and get informal alignment around it, and to decide if it is well-suited for the MEP process[^when-mep]. _MEPs should ideally have at least two, and ideally 3-4 co-authors from different organizations._
2. **Make a proposal via a PR to `myst-enhancement-proposals`**. Use a markdown template to structure your proposal. The `status` should initially be set to `Draft`. Here's a proposed template:
   
   ```
   ---
   mep:
      id: <NNNN - Add when this MEP becomes Active>
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
   
   ## UX implications & migration
   
   <!-- describe how this would improve the UX or functionality of MyST markdown. Describe any deprecations or syntax migration steps that would be needed. -->
   
   ## Questions or objections
   
   <!-- as conversation takes place, list anything that is needed to be resolved and provide links to the conversation where this happened. -->
   
   ## References
   
   <!-- reference other examples you're using for inspiration or to help others learn and understand the proposal. -->
   ```
4. **Discuss and iterate**. Invite discussion from others in the community. Incorporate new ideas as individuals (particularly core team members) raise objections or make suggestions.
   % TODO: Define guidelines for considerations to take during discussion, such as implementation feasibility.
   % TODO: Define policy around what happens if an implementation _cannot_ implement something that has already been merge into the spec.
   % one suggestion here: https://github.com/executablebooks/meta/pull/843#issuecomment-1274555428
5. **Activate decision making**. Once the proposal has stabilized and the author wishes to move forward, do the following:
   - In the MEP frontmatter, set the status as `Active` and add an incremental MEP number (e.g. `id: 0002`). The MEP should no-longer change substantially.
   - **The Core Team** should review the MEP and approve if they wish to accept it.
     - To approve, click `Approve` the GitHub Pull Request UI.
     - To request blocking changes, then click `Request Changes` in the GitHub UI.[^blocking]
   - A MEP may be accepted when all of the following conditions are met:
     - More than five (5) weekdays have passed since the proposal was marked as `Active`.
     - At least two `PR Approvals` from **core team members**.
     - No `Request Changes` from a core team member.
   - If the MEP is accepted:
     - Update its status metadata to `Accepted` and merge the PR.
     - Once a PR is merged, it closes the issue and a decision has been made.
     - The changes in the MEP then become "part of the myst spec" via a Pull Request to `myst-specification` that anyone is welcome to implement.
   - If there are unresolved objections (via `Request Changes` to the PR)
     - The MEP author may restart the voting process after incorporating feedback to resolve the objection, **or** ask the Steering Council to follow the same [decision-making process used for team policy](governance:policy-decision).


[^when-mep]: Below is example text to provide guidance in when to use the MEP process.

    ```
    ## When should I open a MEP?

    The goal of Enhancement Proposals are to align the team on major strategic decisions about MyST Markdown, and to formally record a decision. When deciding whether to propose a MEP, consider whether the importance or complexity of the topic is worth the extra overhead of the MEP process. Ultimately, the most important thing is that we follow principles of open and inclusive discussion, iteration and collaborative writing, and making decisions explicit.

    As a guide, below are examples of topics that warrant a MEP:

    - Changing or extending the syntax or major functionality of MyST.
    - Defining high-level strategy and vision for the language
    - Amending the MEP process itself
    ```
