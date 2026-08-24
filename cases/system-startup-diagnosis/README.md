# Diagnose a System That Starts and Shuts Down

> **Illustrative demo:** This supervised hardware simulation omits fault-staging and reset methods.

## Context

- **Experience type:** Supervised hardware troubleshooting simulation
- **Date:** Illustrative demo date
- **My role:** Acting support technician responsible for safe inspection, approved correction, testing, and documentation
- **Technical areas:** Desktop startup, cooling, thermal protection, hardware safety

## Problem or goal

A desktop started briefly and shut down before the operating system loaded. Internal inspection required power disconnection and electrostatic-discharge precautions. Component replacement remained outside scope until evidence supported it.

## Decision record

| Check or action | Why I chose it | What I found | What changed next |
|---|---|---|---|
| Reproduce the symptom once | Confirm the shutdown pattern | The system received power, began startup, and shut down within seconds | Inspect power delivery and cooling behavior |
| Check the outlet path, power cable, and supply switch | External power is quick and safe to verify | The external path was secure and enabled | Perform an approved internal visual inspection |
| Observe fans during startup | A protective shutdown may follow missing CPU cooling | Case fans moved, and the CPU fan didn't spin | Power down and trace the fan lead |
| Inspect the CPU fan connection | Confirm a power or obstruction issue | The lead was disconnected and the blades moved freely | Seat the lead on the approved header |
| Start twice and check firmware health | Verify stable cooling and startup | The fan ran, firmware showed normal status, and both starts reached sign-in | Close the case and document the result |

## Result and verification

- **Cause:** The CPU cooling fan wasn't connected to its approved motherboard header.
- **Correction:** I seated the fan lead with power removed and routed it clear of the blades.
- **Verification:** The fan ran continuously, firmware showed normal fan status, and the system completed two cold starts.
- **Closing communication:** The reviewer received the cause, safety steps, correction, and repeated startup result.
- **Remaining limitation:** The short test didn't establish long-term thermal performance.

## My contribution

In this demo response, the participant reproduced the symptom, separated external power from cooling theories, followed the safety boundary, found the disconnected lead, completed the approved correction, and verified startup. The reviewer confirmed the allowed work and final state.

## What I learned

- **First theory:** An external power problem seemed possible because the computer wouldn't stay on.
- **Changed direction:** Brief power and fan activity showed that the system received power, while the stationary CPU fan pointed toward cooling protection.
- **Next time:** I would record the exact power and fan sequence during the first controlled reproduction.

## Interview answer

In a supervised hardware simulation, a desktop started briefly and shut down. I verified external power, observed the startup sequence, and saw that the CPU fan wasn't moving. After powering down and following static-safety steps, I reconnected the fan lead and verified normal firmware status and two complete starts. The case taught me to use the timing and physical signs of a failure to narrow the theory safely.

## Evidence

- [Evidence guide](evidence/README.md), which lists safe diagrams and verification checklists

## Sanitization note

This entry contains no real device identifiers, serial numbers, credentials, ticket record, or hidden simulator procedure.
