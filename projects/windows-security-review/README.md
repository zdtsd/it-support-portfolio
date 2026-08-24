# Review a Windows Workstation Security Baseline

> **Illustrative demo:** These observations model a supervised training project and don't describe a production workstation.

## Context

- **Experience type:** Supervised Windows security project
- **Date:** Illustrative demo period
- **Goal:** Review visible update, antivirus, firewall, account, and remote-access status
- **My role:** Perform the checks, prioritize a safe action, verify the final state, and document limitations
- **Scope:** Standard Windows settings and one approved restart; policy bypass and security testing were excluded

## Problem or goal

The project needed a repeatable baseline review that an entry-level technician could perform safely. Every control required a visible status, a short risk explanation, and a next action that respected managed settings.

## Decision record

| Decision or action | Why I chose it | Result | What changed next |
|---|---|---|---|
| Begin with read-only checks | Avoid weakening a healthy control | Antivirus and the active firewall profile were on; the daily account was standard; Remote Desktop was disabled | Review update state |
| Classify managed or hidden details as unknown | A support role doesn't authorize policy bypass | No unsupported change was needed | Document the escalation rule |
| Prioritize the pending update restart | It was the only visible finding and required completion | The reviewer approved a restart window | Save work and restart |
| Recheck all five controls | Confirm the action completed without weakening another control | The restart requirement cleared and the other controls stayed in their approved state | Record the final baseline |

## Result and verification

- **Deliverables:** A five-control status table, priority decision, and final verification record.
- **Testing:** Windows Update showed no remaining restart requirement; antivirus and firewall remained active; account and remote-access states were unchanged.
- **Final result:** The controlled workstation completed its pending update restart and retained the reviewed security controls.
- **Remaining limitation:** This baseline review wasn't a penetration test, policy audit, or malware-forensics assessment.

## My contribution

In this demo response, the participant located each control, recorded its state, connected the state with risk, selected the pending restart as the priority, completed the approved action, and repeated the checks. The reviewer approved the change window and confirmed the final checklist.

## What I learned

- **Important challenge:** A status page may show that policy manages a setting without showing its source.
- **Changed direction:** Healthy controls and a single pending restart supported a narrow action.
- **Next time:** I would record the active network profile first so the firewall result has immediate context.

## Interview answer

In a supervised Windows security project, I reviewed update, antivirus, firewall, account, and remote-access status. I found that installed updates still needed a restart while the other controls were healthy. I coordinated approval, completed the restart, and rechecked every control. The project reinforced the value of documenting managed settings and making only supported changes.

## Evidence

- [Evidence guide](evidence/README.md), which lists safe checklists and cropped status artifacts

## Sanitization note

This entry contains no account name, device identifier, address, policy name, organization detail, log export, or credential.
