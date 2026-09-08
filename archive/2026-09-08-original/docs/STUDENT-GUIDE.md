# Student Guide

## Why this portfolio exists

An interview question often asks for a specific example: a printer problem, a hardware repair, a command-line diagnosis, a security concern, or a time the first theory was wrong. Memory alone is unreliable. This portfolio gives you a searchable record of what you did, why you did it, what happened, and how you verified the result.

Selected classwork becomes evidence you can explain accurately. Routine completion still belongs in the worklog, while stronger activities receive full entries.

## What belongs here

- Short worklog rows for completed tickets, exercises, labs, and projects
- Full case studies that show meaningful troubleshooting decisions
- Lab reports that explain what the observed result proved
- Project summaries with plans, decisions, deliverables, and acceptance tests
- Knowledge-base articles you tested and can explain
- Scripts you genuinely authored or materially improved
- Sanitized evidence that supports a claim
- Reflections that identify mistakes, changed theories, and future improvement

## What doesn't belong here

- Raw ticket exports or copied ticket threads
- Real requester or participant information
- Credentials, internal addresses, hostnames, asset identifiers, or private infrastructure
- Unreviewed screenshots or logs
- Instructor-only fault-staging, deployment, or reset instructions
- Internal remote-support administration or implementation details
- Work you didn't perform presented as your own
- A long collection of class handouts without personal analysis

Read the full [Sanitization Guide](SANITIZATION-GUIDE.md) before adding evidence.

## How much detail is useful

A practical full entry normally answers these questions:

1. What function was failing or being built?
2. What was my role and scope?
3. Which checks or decisions mattered, and why?
4. What did I find or produce?
5. How did I verify the result?
6. What evidence changed my direction?
7. What would I do sooner next time?

Aim for 300 to 600 words and three to six decision rows. Most drafts should take 15 to 25 minutes. Evidence is optional when the written decision record already supports the learning.

Remove details that don't help a reviewer understand those answers. A command belongs in an entry when its output affected the diagnosis. Typing it alone doesn't make it useful evidence.

## Why reasoning matters more than clicks

“I opened Settings and changed a value” doesn't show troubleshooting. A stronger explanation is: “I compared the failing workstation with a known-good workstation, found that the print objects used different communication ports, corrected the mismatched port, and verified the change with current printer status and a successful test page.”

The stronger version shows comparison, cause, action, and verification. It can also be discussed in an interview without depending on a particular software screen.

## Why verification matters

A configuration change isn't proof of resolution. Verification should test the function the user needed and any important related function. Examples include:

- opening the requested file from a detected USB device;
- printing a Windows test page and the user's actual document;
- resolving a name and loading the intended website;
- rebooting after a hardware change and confirming the new component is detected;
- moving a cable and observing the switch relearn the source MAC address;
- confirming a script's output against a known input.

If user acceptance wasn't available, say so. Don't invent confirmation.

## Be honest about the environment

Use accurate labels such as **supervised support activity**, **simulation**, **lab**, **exercise**, or **personal project**. Training can still demonstrate real technical skill. Misrepresenting it as unsupervised production employment weakens the portfolio and creates interview risk.

## Identify your personal contribution

For team work, write separate statements for:

- what you configured, tested, documented, or communicated;
- what a teammate completed;
- what an instructor approved, demonstrated, or staged;
- what the team verified together.

Don't describe the instructor's hidden method for creating a fault. Your portfolio should cover what you observed and diagnosed from the participant side.

## Choose featured work

Your main README and [Interview Evidence Index](../INTERVIEW-INDEX.md) should eventually feature five strong entries. Together, they should show a useful range of:

- end-user support;
- hardware;
- Windows or operating systems;
- networking;
- printers and peripherals;
- security awareness or incident response;
- documentation and communication;
- command-line tools;
- a multi-step project; and
- escalation, collaboration, or uncertainty.

One excellent entry can support several related skills. Quality and explainability matter more than quantity.

## Maintain the portfolio after the program

- Continue adding short worklog rows for relevant learning and projects.
- Add full entries only when they contribute new evidence.
- Recheck links and validation after reorganizing files.
- Remove stale claims you can no longer explain.
- Keep private material private and review every entry before publication.
- Update the introduction and featured set as your skills and goals change.
- Preserve commit history because it shows growth, review, and correction.

For the first contribution cycle, follow [START-HERE.md](../START-HERE.md). For command-by-command Git help, use the [GitHub Workflow Guide](GITHUB-WORKFLOW.md).
