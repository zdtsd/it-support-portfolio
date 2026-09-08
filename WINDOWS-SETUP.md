# Set up your portfolio on Windows

Git saves the history of your files on your computer. GitHub stores the copy you upload online. A **repository**, or **repo**, is your portfolio folder with Git tracking enabled.

Do the setup once, then use [Add a write-up](#6-add-a-write-up) whenever you have new work. This guide uses **Windows PowerShell**, **Git for Windows**, and **Visual Studio Code**. Run commands one line at a time; if one fails, resolve it before continuing. Replace the CAPITALIZED placeholders with your own information.

Already have your own portfolio on GitHub? Install the tools in step 1, then use [Clone an existing portfolio](#clone-an-existing-portfolio).

## 1. Connect with your instructor and install your tools

1. Create or sign in to your account at [GitHub](https://github.com/).
2. Open your instructor's profile, [NFARThom](https://github.com/NFARThom), and select **Follow**. Give your instructor your exact **GitHub username** so they can invite the right account to ITC3.
3. When your instructor sends the repository invitation, open the invitation email, sign in to that same GitHub account, and accept it. Confirm that you can open [ITC3](https://github.com/NFARThom/ITC3).
4. Install [Git for Windows](https://git-scm.com/install/windows). Keep Git Credential Manager enabled and the option that makes Git available from the command line.
5. Install [Visual Studio Code for Windows](https://code.visualstudio.com/docs/setup/windows), using the **User setup** installer. This is where you'll edit and preview your write-ups.
6. Close any open terminal windows. Open **Windows PowerShell** from the Start menu and run:

```powershell
git --version
```

You should see a Git version number. If installation needs an administrator on your training computer, your instructor can help.

GitHub calls the profile connection [following](https://docs.github.com/en/get-started/exploring-projects-on-github/following-people). Access to ITC3 comes from accepting your instructor's separate [repository invitation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository). You can install the tools while waiting for that invitation.

## 2. Get the starter files

1. Open the [ITC3 starter repository](https://github.com/NFARThom/ITC3). Keep the default branch selected to get the current starter.
2. Select **Code → Download ZIP**. This gives you the current files for your own new portfolio. See [GitHub's download instructions](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives) if needed. If you can't access ITC3, ask your instructor for the starter ZIP.
3. Right-click the downloaded ZIP in File Explorer and choose **Extract All**. Open the extracted folders until you can see `README.md`, `WRITEUP-TEMPLATE.md`, and `write-ups` together.
4. Rename the folder containing those files to `it-support-portfolio`.
5. In File Explorer's address bar, enter `%USERPROFILE%`. Create a folder named `GitHub`, then move `it-support-portfolio` into it.

In PowerShell, open that folder and check its contents:

```powershell
Set-Location "$env:USERPROFILE\GitHub\it-support-portfolio"
Get-ChildItem -Force
```

You should see the portfolio files, including `.gitignore`, directly inside this folder. Keep this PowerShell window open for the remaining steps.

## 3. Start Git and make the portfolio yours

Create your local repository on a branch named `main`:

```powershell
git init -b main
```

Set the name and email attached to your work. In GitHub's [email settings](https://github.com/settings/emails), enable **Keep my email addresses private** and copy the exact GitHub-provided `noreply` address. Use it below. These settings apply to this portfolio; they don't sign you in. [GitHub explains commit email settings here](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address).

```powershell
git config user.name "YOUR NAME"
git config user.email "YOUR GITHUB NOREPLY ADDRESS"
git config --get user.name
git config --get user.email
```

Check that the displayed values are yours, then open the folder in VS Code:

```powershell
code .
```

Edit `README.md`: add your name and one or two sentences about your interests and training. Keep the example notice while sample entries are still listed. Save the file with **Ctrl+S**. Use **Ctrl+Shift+V** to [preview Markdown](https://code.visualstudio.com/docs/languages/markdown).

## 4. Create your own GitHub repository

Open [New repository](https://github.com/new) on GitHub and use these settings:

| Setting | What to choose |
| --- | --- |
| Owner | Your own GitHub account |
| Repository name | `it-support-portfolio` |
| Visibility | **Private** while you're preparing your work |
| Add README, .gitignore, or license | Leave these off; the local starter already contains your files |

Select **Create repository**. Keep the new repository's page open. These are the [GitHub settings for uploading an existing local project](https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github).

## 5. Upload your first version

Back in PowerShell, connect your local folder to your new repository. Replace `YOUR-USERNAME` with your GitHub username, or copy your repository's **HTTPS** URL from its setup page:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/it-support-portfolio.git
git remote -v
```

Both displayed URLs should point to **your account and your portfolio**. `origin` is Git's name for this online destination.

Choose the files for your first saved version with [git add](https://git-scm.com/docs/git-add):

```powershell
git status
git add .
git diff --cached --stat
```

Review the list. It should contain your starter documents and write-ups. Keep private ticket details and credentials out of your files. The starter's `.gitignore` keeps local archive and raw-evidence folders out of normal staging.

Now create a **commit**, which saves a version locally, and **push** it to GitHub:

```powershell
git commit -m "Create my IT support portfolio"
git push -u origin main
```

Complete the GitHub sign-in when prompted, using the account that owns this repository. Git Credential Manager handles browser sign-in and two-factor authentication; you can [read about that sign-in process here](https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git?platform=windows).

Refresh your repository page. Your README and files should now appear. Future uploads can use [git push](https://git-scm.com/docs/git-push) because `-u` connected your local `main` branch to GitHub's copy.

## 6. Add a write-up

At the start of each session, open PowerShell and use [git pull](https://git-scm.com/docs/git-pull) to download any changes made on GitHub:

```powershell
Set-Location "$env:USERPROFILE\GitHub\it-support-portfolio"
git pull --ff-only
code .
```

For your first entry, copy the template. Choose a new filename for every later entry so you keep your previous work:

```powershell
Copy-Item .\WRITEUP-TEMPLATE.md .\write-ups\my-first-ticket.md
```

In VS Code, edit the new file using [Start here](START-HERE.md). The same template works for tickets and XP Cyber challenges. Add its link and result to `README.md`, replacing a sample row. Save both files and preview them.

Review and stage your README and write-up changes. This also includes any sample files you removed:

```powershell
git status
git diff
git add README.md write-ups
git diff --cached
```

`git diff --cached` shows everything selected for the next commit, including the new write-up. Once it looks right:

```powershell
git commit -m "Add my first troubleshooting write-up"
git push
git status
```

Use a message describing your actual entry. You should finish with a clean working tree and a branch that's up to date with `origin/main`. Refresh GitHub and open your new write-up to confirm the upload.

Repeat this section for future work. Remove the remaining sample rows and files as you replace them with your own entries. When you're ready to share, a private repository requires you to grant the reader access; review your work before choosing public visibility.

## Clone an existing portfolio

<details>
<summary>Use this route if you or your instructor already created your own portfolio repository on GitHub</summary>

Install the tools in step 1. Then copy your portfolio's HTTPS URL from **Code** on GitHub and use it below. A [clone](https://git-scm.com/docs/git-clone) downloads the files and connects them to their existing Git history and online destination.

If `it-support-portfolio` already exists locally, open that existing copy instead of cloning into it again.

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\GitHub"
Set-Location "$env:USERPROFILE\GitHub"
git clone https://github.com/YOUR-USERNAME/it-support-portfolio.git it-support-portfolio
Set-Location .\it-support-portfolio
git config user.name "YOUR NAME"
git config user.email "YOUR GITHUB NOREPLY ADDRESS"
git remote -v
```

Use the identity guidance in step 3. Check that the remote points to your assigned portfolio.

For a repository containing this starter, continue at **step 6**. Cloning already sets up Git and the remote, so steps 2–5 are complete. If your assigned repository is empty or uses a different layout, ask your instructor for its starting files.

</details>

## If something gets stuck

| What you see | What to do |
| --- | --- |
| `git` isn't recognized | Reopen PowerShell after installation. If it still fails, check the Git installer option for command-line access. |
| `code` isn't recognized | Reopen PowerShell, or open VS Code from Start and use **File → Open Folder** to select your portfolio. |
| `not a git repository` | Check that PowerShell is inside your portfolio folder. For a fresh ZIP setup, complete step 3 there. |
| `Author identity unknown` | Set your name and email in this repository using step 3, then retry the commit. |
| Sign-in fails or access is denied | Check `git remote -v` and the GitHub account used to sign in. Your instructor can help correct a saved sign-in to the wrong account. |
| A push is rejected or `pull --ff-only` can't continue | GitHub and your local copy have different changes. Keep your work and ask your instructor to help bring the copies together. |
| A diff fills the screen and shows `(END)` | Press **Q** to return to PowerShell. |
| GitHub still shows the old version | Save the editor files, then check `git status`. A commit saves locally; the following push uploads it. |
