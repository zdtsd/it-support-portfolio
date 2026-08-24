# Start here

You don't need to know advanced Git or GitHub features to begin. Complete these steps in order and ask for help when a command reports an error.

## 1. Personalize the repository

Open `README.md`. Replace `[Participant Name]` with your name. Keep the starter and demo notice during your first cycle. Replace it with a short portfolio description after your instructor reviews the personalization.

## 2. Update your introduction

Rewrite the professional introduction in your own words. State that the work was completed in a supervised training environment. Don't describe training exercises as unsupervised production employment.

## 3. Add your first worklog row

Open [WORKLOG.md](WORKLOG.md). Add one short row for a completed activity below the demo section. A worklog row is a memory aid and doesn't need to become a full report.

## 4. Choose and copy a template

Choose the template that matches the activity:

- Help-desk ticket or troubleshooting activity: [Ticket Case Study](templates/TICKET-CASE-STUDY.md)
- Hands-on lab: [Lab Report](templates/LAB-REPORT.md)
- Multi-step project: [Project Summary](templates/PROJECT-SUMMARY.md)
- Reusable procedure: [Knowledge-Base Article](templates/KNOWLEDGE-BASE-ARTICLE.md)
- Script you authored or materially improved: [Script README](templates/SCRIPT-README.md)

Copy the template into the matching folder. Use a short descriptive folder name such as `cases/network-printer-offline`, not `case1` or a real ticket number.

## 5. Write the first full entry

Explain the situation, what you personally did, why you chose each major step, the result, and how you verified it. Leave unsupported sections incomplete and mark unknown or unverified items honestly.

## 6. Add only sanitized evidence

Read the [Sanitization Guide](docs/SANITIZATION-GUIDE.md) before adding screenshots, logs, command output, diagrams, or configuration snippets. Never add raw ticket exports. Crop and redact screenshots before they enter the repository.

The optional `local-project-inbox/` folder is ignored by Git and can hold source material during evidence conversion. Create it with `mkdir local-project-inbox`. An ignored folder still needs approved local storage and careful handling.

## 7. Run the validator

From the repository root, run:

On Linux or macOS:

```console
python3 tools/validate_portfolio.py
```

On Windows:

```console
py tools/validate_portfolio.py
```

If your system provides the command as `python` instead, that command is also acceptable. Correct every reported error. The validator catches common problems, but you must still review the work manually.

## 8. Create a meaningful commit

Review the changed files, stage them, and create a commit that describes the result:

```console
git status
git diff
git add WORKLOG.md cases/network-printer-offline
git commit -m "docs: add network printer troubleshooting case"
```

## 9. Push your work

Push the branch shown by `git branch --show-current`:

```console
git push -u origin your-branch-name
```

## 10. Request instructor review

Open a pull request on GitHub. A **pull request** is a review page that compares your branch with the main branch. Complete the privacy and verification checklist in the pull-request template.

If you use GitHub CLI:

```console
gh pr create --fill
```

## 11. Correct review findings

Edit the same branch, run validation again, and commit the corrections separately:

```console
git add cases/network-printer-offline
git commit -m "fix: clarify printer verification steps"
git push
```

A follow-up commit makes the learning and correction visible.

## 12. Add strong work to the interview index

After an entry passes review, link it from [INTERVIEW-INDEX.md](INTERVIEW-INDEX.md) when it provides strong evidence for an interview question. Only your best five to eight entries need to be featured on the main README.

## Your first finish line

You are finished with the first cycle when you have:

- one worklog row;
- one complete, sanitized entry;
- a passing validator run;
- a meaningful commit;
- a reviewed pull request; and
- a correction commit if the review identified an issue.
