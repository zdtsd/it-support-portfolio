# Sanitization Guide

Sanitization is the process of removing or replacing information that should not enter a portfolio. A technically excellent entry isn't publishable when it exposes a person, credential, internal system, or confidential process.

## Never commit these items

- Real user or participant names, unless you are naming yourself intentionally
- Email addresses
- Phone numbers
- Internal ticket links
- Raw ticket exports
- Internal ticket numbers when they can identify a record
- Internal IPv4 or IPv6 addresses
- Internal hostnames or domain names
- Asset tags
- Serial numbers
- Credentials
- API keys
- Tokens
- Private keys or certificates
- Password-reset values
- Internal server paths
- Screenshots containing unrelated tabs, files, notifications, or personal information
- Instructor-only deployment, fault-staging, or reset methods
- Internal remote-support administration or implementation details
- Confidential organization information
- Real production customer information

Don't commit a secret temporarily with the intention of removing it later. Git preserves committed history.

## Safe replacements

Use descriptions that preserve the technical meaning without exposing the source:

| Sensitive value | Safer replacement |
|---|---|
| Requester name | `Example User` or `the user` |
| Ticket number | `sanitized training case` |
| Workstation hostname | `affected workstation` |
| Asset or serial number | `sanitized device identifier` or omit it |
| Internal printer name | `shared network printer` |
| Internal path | `[internal path removed]` |
| Credential | `[credential removed]`; never use a working substitute |

Fictional names such as **Example User** are preferable to real requester names.

## Documentation address ranges

When an example needs an IPv4 address, use an address from a documentation-only range:

- `192.0.2.0/24`
- `198.51.100.0/24`
- `203.0.113.0/24`

These ranges are intended for examples and documentation. Don't transform a real internal address by changing only one digit; replace it completely.

For hostnames, use a clearly fictional name under `example.com`, such as `printer.example.com`.

## Screenshots and images

Before adding a screenshot:

1. Close unrelated applications, tabs, notifications, chats, and file windows.
2. Capture only the smallest area needed to support the claim.
3. Check window titles, browser tabs, bookmarks, taskbars, system trays, usernames, file paths, device names, addresses, and timestamps.
4. Crop the image.
5. Apply permanent redaction. A removable annotation layer can expose the covered content.
6. Export a new flattened image and review it at full size.
7. Remove unnecessary image metadata when practical.
8. Ask a peer or instructor to perform a second review.
9. Explain in the evidence README what the image proves.

Don't add an unreviewed image to Git and plan to clean it later. Files remain in history after a normal deletion.

## Logs, commands, and configuration excerpts

- Include only the lines needed to support the explanation.
- Replace internal addresses, names, paths, and identifiers consistently.
- Remove prompts or command history that reveal usernames or hostnames.
- Don't include full configuration backups.
- Encrypted credentials are still credentials and must stay out of the repository.
- Prefer a short typed excerpt or diagram when raw output contains unrelated data.
- State when output was reconstructed or shortened for publication.

## Student observation versus instructor staging

Portfolio content should describe the participant-facing experience:

- what the participant observed;
- which theories the participant considered;
- which checks the participant performed;
- how evidence changed the participant's direction;
- what the participant corrected or escalated; and
- how the result was verified.

Don't document the hidden instructor method used to create, deploy, or reset the condition. That method isn't the participant's troubleshooting work and may reveal internal training or administration controls.

## Raw evidence staging

If local policy permits temporary raw evidence, keep it outside the repository or inside a deliberately ignored local-only staging folder such as `raw-evidence/`. Treat ignored folders as sensitive: `.gitignore` reduces accidental commits but doesn't secure or encrypt data.

Only a reviewed, cropped, redacted derivative belongs in an entry's `evidence/` directory.

## Pre-commit review

Before every commit:

- [ ] Run `git status` and account for every file.
- [ ] Run `git diff --staged` and read the entire staged change.
- [ ] Run `python3 tools/validate_portfolio.py` (`py` on Windows).
- [ ] Search visually for names, addresses, identifiers, credentials, and internal paths.
- [ ] Open each image at full size and inspect every visible area.
- [ ] Confirm that scenario staging and instructor-only details are absent.
- [ ] Confirm that the experience type and personal contribution are honest.

## If sensitive information was committed

1. Stop pushing or sharing the repository.
2. Notify the instructor or repository owner.
3. Revoke or rotate any credential, token, key, certificate, or reset value immediately through the authorized owner.
4. Determine who may have accessed the repository.
5. Follow the approved history-cleanup or repository-replacement process.
6. Revalidate and review the corrected repository before restoring access.

Deleting the value in a later commit doesn't remove it from earlier history. Don't improvise a destructive history rewrite without coordination.

## Automation limitation

The validator can identify common patterns and unsafe file types, but it can't recognize every name, internal hostname, screenshot detail, subtle identifier, or confidential fact. Manual review remains required.
