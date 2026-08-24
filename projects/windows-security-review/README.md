# Windows Workstation Security Baseline Review

> **Demo training entry.** This completed project summary shows one possible response to a supervised Windows security worksheet. Its observations are illustrative and don't describe a production workstation.

## Experience type

Supervised CompTIA A+ Windows security review.

## Date

Illustrative demo period: 2026-02-23 to 2026-02-24.

## Goal

Review a controlled Windows workstation's visible update, antivirus, firewall, account, and remote-access status. Classify each area, select the safest priority action, and verify the final state.

## Business or training need

A support technician needs to recognize common workstation security controls, explain the risk each control reduces, and respect settings enforced by an administrator. The exercise developed a repeatable baseline review that supports clear escalation.

## Scope

### Included

- Windows Update status
- Virus and threat protection status
- Active firewall profile and status
- Visible account type
- Remote Desktop status
- Priority, approved action, and post-action verification

### Excluded

- Policy bypass
- Unapproved account or service changes
- Malware forensics
- Production security assessment
- Collection of usernames, device identifiers, logs, or organization settings

## Participant's role

In this demo response, the participant performed the visible checks, classified each result, chose the next safe action, completed an approved restart, and documented the verification. The supervising reviewer retained authority over policy and system changes.

## Plan

| Phase | Planned work | Success condition |
|---|---|---|
| Prepare | Confirm scope and use read-only checks first | No unapproved setting changes occur |
| Observe | Review five control areas | Every area has a visible status and risk explanation |
| Prioritize | Compare active findings | One action is selected using impact and urgency |
| Act | Perform only the approved correction | The selected finding is resolved without weakening another control |
| Verify | Recheck each control and record limitations | Final status is clear and repeatable |

## Implementation

I opened the standard Windows security and account settings on the training workstation. I recorded only the status needed for the exercise.

| Control area | Illustrative observation | Classification | Next safe action |
|---|---|---|---|
| Windows Update | Security updates were installed and a restart was pending | Needs action | Save work, obtain approval, restart, and recheck |
| Virus and threat protection | Protection was active with no warning shown | Good | Leave enabled and record the visible status |
| Firewall | The firewall was on for the active network profile | Good | Leave enabled; no rule change was required |
| Account permissions | The daily-use account appeared as a standard account | Good | Keep least-privilege use and escalate if elevated work is needed |
| Remote Desktop | Remote Desktop was disabled | Good | Leave disabled because the exercise showed no approved need |

The pending restart was the only active finding. After approval, I saved the training work, restarted the workstation, returned to Windows Update, and confirmed that the restart requirement had cleared.

## Major decisions

| Decision | Evidence or constraint | Tradeoff |
|---|---|---|
| Start with read-only review | The task was to identify status and risk safely | Some details may remain unavailable when policy manages them |
| Prioritize the pending restart | Other reviewed controls were active and the installed update needed restart completion | Restart required coordination to avoid interrupting work |
| Leave healthy controls unchanged | No evidence supported a firewall, antivirus, account, or remote-access change | The review avoided changes that could create a new risk |
| Document managed or unavailable details | Support staff shouldn't bypass policy | Administrative confirmation may be needed for a complete assessment |

## Challenges

Security pages can show a status without exposing the policy source. The project used four labels: good, risky, unknown, and managed. A managed or unknown result called for documentation and escalation. It didn't authorize a workaround.

## Deliverables

- The completed control-status table in this report
- The priority decision and approved action record
- The [evidence guide](evidence/README.md) for safe supporting artifacts

## Testing and verification

- Reopened Windows Update after restart and confirmed no restart requirement remained.
- Rechecked virus and threat protection and saw no warning.
- Rechecked the active firewall profile and confirmed protection remained on.
- Confirmed the account classification and Remote Desktop status were unchanged.
- Asked the supervising reviewer to confirm that the action stayed within scope.

The checks verify the final visible baseline for this illustrative exercise. They don't provide a penetration test, policy audit, or malware-forensics conclusion.

## Final result

The controlled workstation completed its pending update restart. The reviewed antivirus, firewall, least-privilege account, and remote-access settings remained in their approved state. The project produced a concise baseline record and a clear escalation rule for managed or unknown settings.

## What I did personally

I located each control, recorded its visible state, connected the state with a security risk, selected the pending restart as the priority, completed the approved restart, and repeated the checks. I didn't change policy-managed settings or claim access beyond my assigned role.

## Collaboration

The supervising reviewer approved the restart window and confirmed the final checklist. The participant owned the observation, prioritization, action, and documentation.

## Lessons learned

- A security review needs a visible status, a risk explanation, and a safe next action.
- Healthy security controls should stay enabled unless evidence and approval support a change.
- Managed or hidden settings should be documented and escalated.
- Next time, I would record the active network profile at the beginning so the firewall result has immediate context.

## Interview-ready answer

In a supervised Windows security project, I reviewed update, antivirus, firewall, account, and remote-access status. I found that installed security updates still needed a restart while the other controls were healthy. I chose the restart as the priority, coordinated approval, completed it, and rechecked every control. The project reinforced that safe support work includes documenting managed settings and avoiding unsupported changes.

## Evidence

The [evidence guide](evidence/README.md) explains which artifacts could support this project. The repository includes no fabricated screenshot, event log, account list, or policy export.

## Sanitization confirmation

- [x] All results are identified as illustrative training observations.
- [x] No account name, device identifier, address, policy name, or organization detail appears.
- [x] No credential, key, certificate, log export, or raw system report appears.
- [x] The entry excludes policy bypass and instructor-only implementation details.
- [x] Personal and reviewer responsibilities are separated clearly.
- [x] The entry was reviewed against the [Sanitization Guide](../../docs/SANITIZATION-GUIDE.md).
