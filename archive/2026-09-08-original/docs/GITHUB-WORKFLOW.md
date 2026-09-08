# GitHub Workflow Guide

This guide covers one beginner contribution cycle. Commands run from a terminal. Replace placeholders such as `<repository-url>` and `<branch-name>` with values provided for your repository.

## Key terms

- **Repository:** A project folder tracked by Git.
- **Commit:** A named checkpoint containing selected changes.
- **Branch:** An isolated line of work inside a repository.
- **Remote:** The GitHub copy associated with the local repository, commonly named `origin`.
- **Push:** Send local commits to GitHub.
- **Pull:** Bring remote commits into the local repository.
- **Pull request:** A GitHub review page comparing a branch with the main branch.
- **Merge:** Accept reviewed branch changes into the destination branch.
- **GitHub CLI:** The `gh` command, which creates repositories and pull requests from a terminal.

## 1. Clone the repository

Cloning creates a local copy and configures its remote:

```console
git clone <repository-url>
cd <repository-folder>
```

With GitHub CLI, use the repository's `OWNER/NAME` form:

```console
gh auth login
gh repo clone <owner>/<repository>
cd <repository>
```

Never place a token or password directly in the clone URL.

## 2. Pull current work

Before starting, update the local default branch:

```console
git switch main
git pull --ff-only
```

`--ff-only` prevents Git from creating an unexpected merge commit during a routine pull. Ask for help if Git reports that it can't fast-forward.

## 3. Create a branch

Use a short descriptive name:

```console
git switch -c docs/network-printer-case
```

Don't place a real ticket number, requester name, or confidential identifier in the branch name.

## 4. Copy the correct template

For a ticket case on Linux or macOS:

```console
mkdir -p cases/network-printer-offline
cp templates/TICKET-CASE-STUDY.md cases/network-printer-offline/README.md
```

In PowerShell:

```powershell
New-Item -ItemType Directory -Force cases/network-printer-offline
Copy-Item templates/TICKET-CASE-STUDY.md cases/network-printer-offline/README.md
```

Use a descriptive folder name. Avoid `case1`, `stuff`, requester names, and real ticket numbers.

## 5. Edit Markdown

Complete the prompts in the copied file. Remove unused instructions. Update [WORKLOG.md](../WORKLOG.md), and add the entry to the [Interview Evidence Index](../INTERVIEW-INDEX.md) only when it is a strong reviewed example.

## 6. Review changes

Check which files changed and inspect the content:

```console
git status
git diff
```

Confirm that the diff contains only the intended entry, worklog, evidence, and index changes.

## 7. Run validation

```console
python3 tools/validate_portfolio.py
```

Use `py tools/validate_portfolio.py` on Windows, or `python` when that is the installed command. Correct all errors. Then perform the manual checks in the [Sanitization Guide](SANITIZATION-GUIDE.md), especially for screenshots.

## 8. Stage files

Stage only the files that belong to this change:

```console
git add WORKLOG.md cases/network-printer-offline
git status
```

Avoid `git add .` until you can explain every untracked and modified file shown by `git status`.

## 9. Commit with a meaningful message

```console
git commit -m "docs: add network printer troubleshooting case"
```

Useful examples include:

- `docs: add network printer troubleshooting case`
- `docs: add managed switch commissioning lab`
- `docs: update interview evidence index`
- `fix: clarify DNS verification steps`
- `fix: remove identifying information from screenshot`

“Updated stuff” is poor because it doesn't tell a reviewer what changed, why the commit exists, or whether the change is documentation, a correction, or a new feature.

## 10. Push the branch

```console
git push -u origin docs/network-printer-case
```

The `-u` option connects the local branch to its remote branch so later pushes can use `git push`.

## 11. Open a pull request

On GitHub, open a pull request from your branch into `main`. Complete every applicable item in the pull-request template. Add a short summary of the entry, verification, and any limitations.

GitHub CLI can create the pull request from the current branch and fill its title and description from the commit:

```console
gh pr create --fill
gh pr view --web
```

Review and complete every pull-request checklist item before submitting it.

## 12. Respond to feedback

Read each review comment. Ask when a requested change is unclear. Make corrections on the same branch, rerun validation, and review the diff.

You can check the pull request and automated validation from the terminal:

```console
gh pr status
gh pr checks
```

## 13. Make a correction commit

```console
git add cases/network-printer-offline
git commit -m "fix: clarify printer verification steps"
git push
```

The pull request updates automatically. Don't open a second pull request for the same correction.

## 14. Merge after approval

Merge only after required technical and privacy reviews are complete and the validation workflow passes. Use the merge method chosen by the instructor or repository owner.

After merge, update your local copy:

```console
git switch main
git pull --ff-only
```

Delete the old branch only after confirming its work is safely merged.

## When to stop and ask for help

Stop before proceeding when:

- Git reports a merge conflict;
- validation identifies private data you don't understand;
- a credential or secret may have been committed;
- the diff contains files you didn't intend to change;
- a push would overwrite remote work;
- you are unsure whether evidence is safe to publish; or
- the requested correction would misrepresent what you did.
