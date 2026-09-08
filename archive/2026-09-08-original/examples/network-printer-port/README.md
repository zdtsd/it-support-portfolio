# Restore Printing by Correcting a Workstation Port

> **Illustrative demo:** This supervised example shows the practical entry standard and doesn't claim participant experience.

## Context

- **Experience type:** Supervised support simulation
- **Date:** Illustrative demo date
- **My role:** Acting support technician responsible for diagnosis, correction, testing, and communication
- **Technical areas:** Windows printing, network printers, configuration comparison

## Problem or goal

One Windows workstation intermittently showed a shared printer as offline. Other workstations could print, so the impact appeared limited to one print object or communication path. Changes to the printer and network infrastructure were outside scope unless broader evidence supported them.

## Decision record

| Check or action | Why I chose it | What I found | What changed next |
|---|---|---|---|
| Confirm scope with a known-good workstation | Separate a shared outage from a local problem | The known-good workstation printed successfully | Focus on the affected workstation |
| Review the affected queue | Check for paused or blocked jobs | The queue wasn't paused and no job explained the offline state | Compare printer configuration |
| Compare driver and port properties | A local mismatch could explain the one-workstation scope | Drivers matched, but the affected workstation used a different automatically discovered port | Confirm the approved standard port before changing it |
| Select the approved port and print a test page | Correct the supported difference and test the original function | Status changed to ready and the test page printed | Document the result and monitor for recurrence |

## Result and verification

- **Cause:** The workstation's print object used a mismatched communication port.
- **Correction:** I selected the approved standard port used by known-good systems.
- **Verification:** The printer showed ready status, the queue cleared, and a Windows test page printed successfully.
- **Closing communication:** The reviewer received the cause, correction, test result, and instruction to report any recurring offline state.
- **Remaining limitation:** A short test can't guarantee that an intermittent symptom will never return.

## My contribution

In this demo response, the participant confirmed scope, compared the affected and known-good configurations, made the approved port change, ran the test, and wrote the closing update. The supervising reviewer confirmed the allowed configuration and observed the result.

## What I learned

- **First theory:** A shared printer or network outage seemed possible from the user's description.
- **Changed direction:** Successful printing from another workstation established a local scope.
- **Next time:** I would confirm scope and compare the communication port early.

## Interview answer

In a supervised support example, one workstation showed a shared printer offline while other systems could print. I confirmed the limited scope, compared its print configuration with a known-good workstation, and found a mismatched port. I selected the approved port and verified ready status and a successful test page. The case reinforced the value of using a known-good comparison before changing shared infrastructure.

## Evidence

- [Evidence guide](evidence/README.md), which explains safe configuration and verification artifacts

## Sanitization note

This entry contains no real names, printer identifiers, addresses, ticket records, credentials, or instructor setup details.
