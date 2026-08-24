# Instructor Guide

## Purpose

This repository is the instructor-owned canonical starter for participant IT support portfolios. It is designed to turn supervised tickets, labs, exercises, projects, knowledge-base work, and scripts into evidence participants can retrieve and explain during interviews.

The system deliberately separates:

- **worklog memory**, which records every completed activity briefly;
- **full entries**, which explain meaningful work; and
- **featured evidence**, which presents approximately five to eight strong reviewed examples.

This prevents the portfolio from becoming either an empty showcase or an unfiltered archive of classwork.

## Recommended rollout: one repository per participant

Create a separate private repository for each participant from this canonical template. This model is preferred because it provides:

- clear ownership of content and commit history;
- a clean record of the participant's revisions and growth;
- stronger privacy isolation between participants;
- simpler transfer or continued maintenance after the cohort;
- an easier path to a participant-controlled public portfolio; and
- fewer branch, permission, and merge conflicts.

When GitHub's template feature is available, enable **Template repository** on the canonical repository. Create each participant repository with **Include all branches** disabled unless there is a deliberate reason to distribute non-default branches.

## Pilot alternative: shared private repository

A pilot may use one private repository with a dedicated branch and pull request for each participant. Use a consistent branch naming scheme that doesn't expose unnecessary personal information. Participants should not edit another participant's branch.

The shared model is suitable for a short Git workflow pilot, but it has important limits:

- collaborators may be able to view every branch and pull request;
- commit history and ownership are harder to separate;
- accidental cross-participant edits are more likely;
- later public presentation requires migration into separate repositories; and
- privacy impact is broader when one branch contains a problem.

For those reasons, use the shared approach only as a temporary private pilot. Separate repositories remain the recommended final portfolio model.

## Private-first publication model

1. Create or receive the repository privately.
2. Add worklog rows and full entries during training.
3. Review technical accuracy, personal contribution, evidence, and sanitization.
4. Correct findings in follow-up commits.
5. Select featured work only after review.
6. Consider public visibility only after a final repository-wide privacy review and participant approval.

No participant should be required to publish personal work publicly as a condition of learning the workflow.

## Suggested weekly cadence

- Every completed activity receives a brief worklog row.
- One meaningful activity becomes a full entry.
- One entry receives instructor or peer review.
- Technical or privacy corrections are made in a follow-up commit.
- The interview index is updated periodically after enough strong work has accumulated.

This cadence creates useful evidence without requiring a full report for every routine task.

## Review workflow

1. Participant works on a descriptive branch.
2. Participant runs the validator and performs a manual privacy review.
3. Participant opens a pull request and completes the checklist.
4. Reviewer applies the [Review Rubric](REVIEW-RUBRIC.md).
5. Reviewer identifies required technical, evidence, wording, or privacy changes.
6. Participant makes a correction commit on the same branch.
7. Reviewer confirms the correction and approves the merge.
8. Strong entries may later be added to the interview index and root README.

Any credential, private key, personal data, raw ticket export, or internal infrastructure exposure makes the entry **not publishable** until corrected. If a live secret is committed, follow the organization's incident process and rotate or revoke it; deletion from the latest file isn't sufficient by itself.

## Teach Git gradually

Introduce only the concepts needed for the current cycle:

1. Repository, file, and Markdown
2. Status, diff, stage, and commit
3. Pull and push
4. Branch and pull request
5. Review comment and correction commit
6. Merge and sync

Avoid beginning with rebasing, history rewriting, complex conflict resolution, or advanced automation. Those topics can be introduced when a real need appears.

## Handle corrections as learning evidence

Ask participants to fix review findings in a new commit. This keeps the correction visible and avoids unnecessary history rewriting. Useful correction messages include:

- `fix: clarify DNS verification steps`
- `fix: remove identifying information from screenshot`
- `fix: distinguish team and individual contributions`

Reserve history rewriting for an approved privacy or secret-removal procedure.

## Worklog entry versus full entry

| Use a worklog row when… | Create a full entry when… |
|---|---|
| The task was routine or repeated | The troubleshooting required meaningful decisions |
| The result can be remembered in one sentence | Evidence changed the initial theory |
| It adds activity history but little new skill evidence | The work demonstrates a new technical area |
| There isn't enough publishable evidence for a case | The participant can explain personal contribution and verification |
| A similar full entry already exists | The work supports a likely interview question |

## Suggested minimum final portfolio

A reasonable completion target is:

- an accurate introduction and training disclosure;
- a current worklog;
- five to eight featured, reviewed full entries;
- an interview index that covers common support questions;
- a skills matrix supported by links;
- at least one example of troubleshooting reasoning and changed direction;
- at least one example of clear user or technical communication;
- at least one multi-step project, substantial lab, KB article, or documented script; and
- a final repository-wide sanitization review.

Adjust the technical mix to the participant's actual opportunities. Don't require unsupported categories to fill a table.

## Avoid excessive documentation work

- Use the worklog for routine tasks.
- Target about one full entry per active training week, not one per ticket.
- Permit short evidence excerpts. Full logs often contain unrelated or private details.
- Review one technical and one communication improvement at a time when a draft is developing.
- Let one strong entry support several interview questions.
- Focus feedback on reasoning, verification, personal contribution, and privacy. Decorative formatting has lower priority.

## Cohort completion and ownership

For separate repositories, confirm that the participant has appropriate ownership or a documented transfer/export path. Remove instructor or organization access when policy requires it. Record whether the repository will remain private or undergo a final review for public presentation.

For a shared pilot, help the participant copy approved content and relevant authored history into a new participant-controlled repository. Don't transfer other participants' branches, comments, or evidence.

## Manual GitHub settings

These settings may require an owner or administrator:

- Keep the canonical repository private while the program and review process are being established.
- Enable **Template repository** when the account and repository type support it.
- Set the default branch to `main`.
- Add a branch ruleset that requires pull requests for participant repositories when that will not block beginner learning.
- Require the portfolio validation workflow before merge after it has run successfully on the repository.
- Limit GitHub Actions permissions to read repository contents unless a later workflow has a documented need for more.
- Restrict who can change repository visibility, rules, collaborators, secrets, and Actions settings.
- Consider disabling force pushes and branch deletion on the default branch.
- Configure repository description and topics from the suggestions in the final implementation handoff.

Repository security settings should match current organization policy. Don't enable public visibility automatically.

## Creating a repository from the template

When template repositories are supported:

1. Open the canonical repository on GitHub.
2. Select **Use this template** and create a new repository.
3. Choose the participant-controlled owner approved for the program.
4. Use a neutral repository name suitable for later presentation.
5. Select **Private**.
6. Don't copy non-default branches unless they are intentionally part of the starter.
7. Confirm the validator runs before the first participant assignment.

If template creation is unavailable, clone the canonical repository, create a new empty private repository, replace the remote, and push only after confirming no instructor-only history or settings will transfer.
