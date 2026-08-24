# [Participant Name] | IT Support Portfolio

> **ITC3 starter and demo:** This repository is a working example of an employment-ready IT support portfolio. It includes completed demo entries, reusable templates, beginner Git instructions, privacy controls, and an automated validator. Start with this page, then follow [START-HERE.md](START-HERE.md).

## What this repository is

This is the instructor-owned foundation for NFAR IT/Cyber participant portfolios. It shows how to turn completed help-desk tickets, labs, exercises, projects, knowledge-base articles, and scripts into clear evidence of technical work.

The repository has two jobs:

1. It gives participants a safe structure for recording work throughout training.
2. It provides a quick evidence library for interview preparation.

The completed entries below are illustrative. They show the expected detail, reasoning, verification, and privacy standard. Replace them with your own reviewed work as your portfolio develops.

## What it can do for you

Before an interview, you can use the [Interview Evidence Index](INTERVIEW-INDEX.md) to find a relevant example quickly. Each full entry helps you recall:

- the situation and scope;
- your responsibility;
- the evidence you collected;
- why you chose each important step;
- what you changed;
- how you verified the result; and
- what you learned.

That record helps you answer questions about networking, printers, hardware, Windows, security, command-line tools, documentation, collaboration, and incorrect first theories with specific evidence.

## Professional introduction

I am an emerging IT support professional developing practical skills in troubleshooting, hardware, operating systems, networking, security, documentation, and customer communication. This portfolio shows how I approach technical problems, what I personally contributed, how I verified results, and what I learned.

> Hands-on IT support work completed in a supervised enterprise-style training environment. Entries are sanitized and contain no production customer data or confidential organizational information. Each entry identifies whether the experience was a simulation, lab, exercise, supervised support activity, or personal project.

## Featured demo evidence

These eight entries form a populated example portfolio. They don't claim participant experience. A personalized portfolio should eventually feature five to eight of its strongest reviewed entries.

| Featured entry | Experience type | Technical areas | One-sentence proof |
|---|---|---|---|
| [Network printer port troubleshooting](examples/network-printer-port/README.md) | Illustrative case study | Printers, Windows, networking | Compared a failing workstation with known-good systems, corrected the communication port, and verified a test print |
| [Browser connectivity troubleshooting](examples/browser-connectivity/README.md) | Illustrative case study | Windows, networking, command line | Separated adapter, IP, proxy, DNS, and hosts-file behavior before correcting the browser traffic path |
| [Switch MAC-learning lab](examples/switch-mac-learning/README.md) | Illustrative lab | Managed switching, Ethernet | Moved a workstation connection and verified that the switch relearned the source MAC on the new port |
| [Command-line troubleshooting decisions](labs/command-line-troubleshooting/README.md) | Illustrative exercise | Windows, command line, networking | Selected commands by the question each output could answer and documented their limits |
| [DHCP DORA process analysis](labs/dhcp-dora-analysis/README.md) | Illustrative lab | IPv4, DHCP, protocol analysis | Explained the state change created by every message in the lease sequence |
| [System startup diagnosis](cases/system-startup-diagnosis/README.md) | Illustrative case study | Hardware, power, cooling | Used the shutdown pattern and fan behavior to find a disconnected CPU fan lead and verify stable startup |
| [Windows security baseline review](projects/windows-security-review/README.md) | Illustrative project | Windows, security, change control | Reviewed five controls, prioritized an approved update restart, and rechecked the baseline |
| [Printer troubleshooting guide](knowledge-base/printer-troubleshooting-guide/README.md) | Illustrative KB article | Printers, documentation, escalation | Connected five common printer symptoms with safe tests, corrections, and verification |

Use the [Interview Evidence Index](INTERVIEW-INDEX.md) to find these examples by interview question.

## Technical areas

- End-user support and ticket documentation
- Computer hardware, startup, and peripherals
- Windows and operating-system support
- IPv4, DHCP, DNS, browser, and local connectivity troubleshooting
- Network printers, queues, ports, and print quality
- Ethernet switching and source-MAC learning
- Security baselines, safe changes, and escalation
- Command-line troubleshooting and verification
- Knowledge-base writing and technical communication
- Projects, collaboration, and reflective improvement

## Tools and technologies

Replace this demo list with tools you have actually used and can discuss:

- Windows Settings, Control Panel, Device Manager, Event Viewer, and Task Manager
- Command Prompt, PowerShell, `ipconfig`, `ping`, `tracert`, `nslookup`, and `netstat`
- Printer properties, queues, ports, internal status pages, and test pages
- Managed-switch command-line interfaces
- Firmware health screens and approved hardware safety tools
- Git, GitHub, GitHub CLI, Markdown, and Python

## Get your own private portfolio

The preferred setup gives each participant a separate private repository. You own the commit history, privacy decisions, and final presentation. Your instructor may create the repository for you, or you can create one from this template.

### Option 1: Create a repository from the template with GitHub CLI

Install [Git](https://git-scm.com/downloads) and [GitHub CLI](https://cli.github.com/), then sign in:

```console
gh auth login
gh auth status
```

When `NFARThom/ITC3` has been enabled as a GitHub template, create and clone a private repository:

```console
gh repo create <github-username>/it-support-portfolio --private --template NFARThom/ITC3 --clone
cd it-support-portfolio
git config user.name "Your Name"
git config user.email "YOUR_GITHUB_NOREPLY_EMAIL"
git switch -c docs/personalize-portfolio
```

Replace `<github-username>` with your GitHub username. Use an email choice shown in your GitHub email settings. A GitHub no-reply address can keep a personal address out of commit metadata.

### Option 2: Clone a private repository your instructor assigned

```console
gh auth login
gh repo clone <owner>/<assigned-repository>
cd <assigned-repository>
git config user.name "Your Name"
git config user.email "YOUR_GITHUB_NOREPLY_EMAIL"
git switch -c docs/personalize-portfolio
```

Your instructor will provide the owner and repository name.

### Make and submit your first change

Edit this README, add your first worklog row, and run the validator:

```console
python3 tools/validate_portfolio.py
git status
git diff
git add README.md WORKLOG.md
git commit -m "docs: personalize portfolio introduction"
git push -u origin docs/personalize-portfolio
gh pr create --fill
```

On Windows, `py tools/validate_portfolio.py` may be the available validator command. Keep the repository private while it contains training work. Ask your instructor to review technical accuracy and sanitization before making any entry public.

For a complete branch, commit, push, correction, and merge walkthrough, use the [GitHub Workflow Guide](docs/GITHUB-WORKFLOW.md).

## Create a local project inbox

You can keep source projects in a local intake folder while you turn them into sanitized portfolio evidence:

```console
mkdir local-project-inbox
git check-ignore -v local-project-inbox/test-file
```

The tracked `.gitignore` excludes `local-project-inbox/` at any depth. Files in that folder won't appear in normal Git staging. An ignored folder isn't a secure vault, so keep sensitive source material only on an approved device and review every derivative before moving it into a tracked portfolio folder.

## Explore the portfolio

| Resource | Purpose |
|---|---|
| [Start Here](START-HERE.md) | Complete the first portfolio entry without prior GitHub portfolio experience |
| [Worklog](WORKLOG.md) | Record every completed ticket, lab, exercise, and project in one short row |
| [Interview Evidence Index](INTERVIEW-INDEX.md) | Match interview questions to the strongest evidence |
| [Skills Matrix](SKILLS-MATRIX.md) | Link technical skills to entries that prove them |
| [Case studies](cases/README.md) | Document help-desk and troubleshooting work |
| [Labs](labs/README.md) | Explain hands-on practice and what the results proved |
| [Projects](projects/README.md) | Present larger, multi-step work |
| [Knowledge base](knowledge-base/README.md) | Write reusable support procedures |
| [Scripts](scripts/README.md) | Document scripts personally authored or materially improved |
| [Student Guide](docs/STUDENT-GUIDE.md) | Understand what belongs in the portfolio and why |
| [Sanitization Guide](docs/SANITIZATION-GUIDE.md) | Remove private, identifying, and instructor-only information |
| [GitHub Workflow Guide](docs/GITHUB-WORKFLOW.md) | Follow the beginner branch, commit, push, and review cycle |
| [Review Rubric](docs/REVIEW-RUBRIC.md) | Check technical quality, evidence, privacy, and interview usefulness |
| [Interview Preparation Guide](docs/INTERVIEW-PREP.md) | Turn full entries into concise spoken answers |
| [Demo Content Notes](docs/DEMO-CONTENT-NOTES.md) | Understand how the illustrative entries were derived and how to replace them |

## The three documentation levels

1. **Worklog:** Every completed activity receives a brief row in [WORKLOG.md](WORKLOG.md). This is your complete activity memory.
2. **Full entry:** Meaningful work becomes a case study, lab report, project summary, knowledge-base article, or script README. During active training, a normal target is about one full entry per week.
3. **Featured evidence:** Five to eight reviewed entries appear here and in [INTERVIEW-INDEX.md](INTERVIEW-INDEX.md). Together, they should show a useful range of support skills.

## Before publishing anything

Start privately. Review every entry and evidence file for names, contact information, ticket identifiers, internal addresses, credentials, asset information, private infrastructure, and unrelated screen content. Automated validation helps, and manual review remains required. Follow the complete [Sanitization Guide](docs/SANITIZATION-GUIDE.md).

## Personalization checklist

- [ ] Replace `[Participant Name]` in the title.
- [ ] Rewrite the professional introduction in your own voice.
- [ ] Keep the supervised training disclosure accurate.
- [ ] List only tools and skills you've actually used.
- [ ] Add your first row to [WORKLOG.md](WORKLOG.md).
- [ ] Copy the right template and create your first full entry.
- [ ] Replace demo entries with reviewed personal evidence over time.
- [ ] Run `python3 tools/validate_portfolio.py` before every pull request.
- [ ] Keep the repository private until technical and privacy review are complete.

## For instructors

This repository is the canonical ITC3 starter. The preferred rollout gives each participant a separate private repository created from this template. See the [Instructor Guide](docs/INSTRUCTOR-GUIDE.md) for rollout options, weekly cadence, review practices, and repository settings.
