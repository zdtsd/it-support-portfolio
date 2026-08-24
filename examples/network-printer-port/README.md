# Network printer intermittently offline from one workstation

> **Starter example - not participant work.** This fictionalized supervised-support example demonstrates the expected structure and level of technical explanation. Replace it with reviewed personal evidence over time.

## Experience type

Sanitized supervised-support example

## Date

Not applicable - starter example

## Role

Tier 1 technician responsible for isolating a workstation-specific printing problem, making an approved configuration correction, and verifying output.

## Technical areas

- Windows print configuration
- Network printer communication
- Known-good comparison
- Customer-facing documentation

## Tools used

- Windows Printers & scanners
- Printer properties and port configuration
- PowerShell `Get-Printer` and `Get-PrinterPort`
- Windows test page

## User report

A shared network printer intermittently appeared offline from one Windows workstation. Other workstations continued printing normally. A temporary network check sometimes appeared to coincide with recovery, but the symptom returned.

## Scope and environment

The impact was limited to one workstation and one shared printer in a supervised training environment. Other users could print, so the investigation began with the affected workstation's print object, driver, queue, and communication path. No printer or network infrastructure change was supported by the scope.

No production identifiers, addresses, printer names, or ticket records are used in this example.

## Initial observations

- **Observed:** Other workstations could print to the same device.
- **Observed:** The affected workstation's printer object alternated between offline and ready states.
- **Not yet established:** A successful ping didn't prove that Windows was sending print jobs through the correct printer port.
- **Safety or permission boundary:** Only the affected workstation's approved print configuration was in scope.

## Troubleshooting process

| Step | Reason for Checking | Result | Next Decision |
|---|---|---|---|
| Confirm printer operation from a known-good workstation | Separate a shared printer or network outage from a workstation-specific problem | Known-good workstation printed successfully | Inspect the affected workstation and leave the working printer unchanged |
| Review queue and printer status | Determine whether a stuck job or paused queue explained the offline state | Queue wasn't paused and contained no blocking job | Compare printer-object configuration |
| Collect printer name, driver, status, and port with PowerShell | Create an exact configuration record before changing anything | The driver matched the working systems, but the port name differed | Inspect the port type and communication target |
| Compare the affected port with a known-good workstation | Use a working baseline to identify a meaningful mismatch | The affected print object used an automatically discovered port; known-good systems used the approved standard network port | Reassign the print object to the approved known-good port |
| Apply the approved port correction | Restore the same communication path used by working systems | Printer status changed to ready | Test actual output and watch for immediate recurrence |
| Print a Windows test page | Verify end-to-end rendering, spooling, communication, and physical output | Test page printed successfully | Record the result and request normal-use confirmation |

## Root cause

The affected workstation's printer object used a mismatched automatically discovered communication port. Known-good workstations used the approved standard network port. This difference explained why the symptom was limited to one workstation.

## Resolution

The print object was reassigned to the approved known-good network port. No printer hardware, shared infrastructure, or driver package was changed.

## Verification

- **Original function tested:** Submitted a Windows test page through the corrected print object.
- **Observed result:** Windows showed the printer ready, the job cleared the queue, and the page printed successfully.
- **Related function checked:** A known-good workstation continued printing normally.
- **User or approved-proxy confirmation:** The exercise owner confirmed the expected printed output; longer-term observation would be required before claiming that an intermittent condition can't recur.

## Customer-facing closing note

> I found that this workstation was using a different printer communication port than the working systems. I updated it to the approved port and verified that the printer showed ready status and produced a successful test page. Please report the issue again if the printer returns to an offline state so the recurrence can be documented.

## Commands and tools used

| Command or tool | Purpose | Relevant result |
|---|---|---|
| `Get-Printer` | Record printer object, driver, port, and status | Confirmed the driver matched but the port differed |
| `Get-PrinterPort` | Inspect the configured port type and target | Confirmed a mismatched automatically discovered port |
| Printer properties | Compare and apply the approved port selection | Print object used the known-good communication path |
| Windows test page | Verify end-to-end printing | Page printed and the queue cleared |

Command output was summarized to protect printer names and network details.

## What I did personally

In this example, the technician confirmed the limited scope, recorded the affected configuration, compared it with a known-good workstation, identified the port mismatch, applied the approved workstation-level correction, ran the test print, and wrote the closing note.

## Collaboration or escalation

The technician used an approved known-good workstation as a comparison and confirmed the expected configuration with the exercise owner. No infrastructure escalation was required. A recurrence after the observation period would require a new timestamped status capture before additional changes.

## Reflection

- **What did I initially suspect?** The offline wording made a general network reachability problem seem plausible.
- **What evidence changed my direction?** Other workstations printed successfully, and the affected printer object used a different port.
- **What would I check sooner next time?** I would record and compare the printer driver and port before using a temporary ping workaround.
- **What did I learn?** Reachability and the Windows print object's configured communication path are related but not equivalent.
- **What technical wording would I improve?** I would say “mismatched printer port configuration.” The phrase “the network was wrong” is too broad.

## Interview-ready answer

In a supervised support example, one Windows workstation intermittently showed a shared printer as offline while other workstations could print. I compared its printer properties and port configuration with a known-good system and found that it used a mismatched automatically discovered port. I reassigned it to the approved network port, confirmed ready status, and produced a successful test page. The experience reinforced that a ping result doesn't prove the print queue is using the correct communication path.

## Evidence

See the [evidence guidance](evidence/README.md). No screenshot or raw command output is included because evidence should never be fabricated for a starter example.

## Sanitization confirmation

- [x] No real requester, participant, or unrelated person is named.
- [x] No email address, phone number, internal link, or raw ticket number is present.
- [x] No internal IP address, hostname, domain, asset tag, or serial number is present.
- [x] No credential, token, key, certificate, reset value, or secret is present.
- [x] No unreviewed screenshot is included.
- [x] Instructor-only staging, reset, and remote-support implementation details are excluded.
- [x] The entry is clearly labeled as a supervised demo and makes no participant-experience claim.
