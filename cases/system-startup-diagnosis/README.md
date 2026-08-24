# Diagnose a System That Starts and Shuts Down

> **Demo training entry.** This fictionalized case models a completed hardware troubleshooting report from a supervised simulation. It omits scenario setup and reset methods.

## Experience type

Supervised CompTIA A+ hardware troubleshooting simulation.

## Date

Illustrative demo date: 2026-02-16.

## Role

Acting support technician responsible for reproducing the symptom, inspecting the training workstation safely, correcting the approved hardware connection, verifying startup, and documenting the result.

## Technical areas

- Desktop power and startup
- Cooling and thermal protection
- Internal cable inspection
- Safe hardware change control
- User communication

## Tools used

- Visual and physical inspection for cable and fan status
- Firmware health screen for post-change status
- Approved electrostatic-discharge precautions for internal work

## User report

A desktop started briefly and then shut itself down before the operating system loaded.

## Scope and environment

The issue affected one simulated desktop in a controlled training environment. The work was limited to observation, approved internal connection checks, and startup verification. No production hardware, account, ticket record, or organization detail was involved.

## Initial observations

- **Observed:** The power indicator and case fans activated briefly, then the system shut down before loading the operating system.
- **Unproven:** The brief startup didn't establish whether the fault involved external power, the power supply, cooling, memory, or another protected component.
- **Safety or permission boundary:** Internal inspection began only after shutdown, power disconnection, and electrostatic-discharge preparation. Component replacement was outside scope unless inspection and testing supported it.

## Troubleshooting process

| Step | Reason for Checking | Result | Next Decision |
|---|---|---|---|
| Reproduce the startup symptom once | Confirm the report and capture the shutdown pattern | The system received power, began startup, and shut down within seconds | Inspect power delivery and visible cooling behavior |
| Check the outlet path, power cable, and supply switch | A loose external connection can cause startup failure and is quick to check | The external path was secure and the power supply switch was on | Continue with an approved internal visual inspection |
| Observe fan behavior during the brief startup | A system may shut down protectively when CPU cooling isn't operating | Case fans moved, but the CPU cooling fan didn't spin | Power down and trace the CPU fan lead |
| Inspect the CPU fan connection with power removed | Confirm whether the fan lacked power or was mechanically blocked | The fan lead was disconnected from its approved motherboard header; the blades moved freely | Reconnect the lead and inspect cable clearance |
| Reconnect the fan lead and inspect the work area | Restore the intended cooling connection without introducing a cable obstruction | The connector was seated and the lead was clear of the fan | Perform controlled startup verification |
| Start the system and check fan and firmware status | Confirm stable power-on and cooling before loading the operating system | The CPU fan spun continuously, firmware showed normal fan status, and startup continued | Load the operating system and repeat a cold-start test |

## Root cause

The CPU cooling fan had no electrical connection to its approved motherboard header. The system began to power on, detected inadequate cooling operation, and shut down protectively. The disconnected lead, stationary fan, and stable startup after reconnection supported the conclusion.

## Resolution

With the system powered off and disconnected, I seated the CPU fan lead on the approved header and routed the cable clear of the fan. No component replacement was required.

## Verification

- **Original function tested:** Started the workstation from a fully powered-off state twice.
- **Observed result:** The CPU fan ran continuously and the workstation reached the operating-system sign-in screen on both starts.
- **Related function checked:** Firmware health status showed normal fan operation and no thermal warning.
- **User or approved-proxy confirmation:** The supervising reviewer confirmed the simulated workstation stayed running and the documented result matched the observed behavior.

## Customer-facing closing note

> I found that the processor cooling fan wasn't receiving power because its cable wasn't seated. I powered the system down, reconnected the fan safely, and checked the cable path. The computer completed two starts, the fan remained active, and the system reached the sign-in screen without a warning. Please report any new shutdown, unusual fan noise, or heat warning.

## Commands and tools used

| Command or tool | Purpose | Relevant result |
|---|---|---|
| External connection inspection | Confirm the outlet, power cable, and supply switch | External power was connected and enabled |
| Internal visual inspection | Check CPU fan power and physical obstruction | Fan lead was disconnected and the fan moved freely |
| Firmware health screen | Check fan status after correction | Fan status was normal with no thermal warning |

No command-line tool was needed for a fault that occurred before the operating system loaded.

## What I did personally

In this demo response, the participant reproduced the symptom, separated external power from cooling theories, followed the safety boundary, identified the disconnected fan lead, performed the approved correction, ran the verification checks, and wrote the closing note.

## Collaboration or escalation

The supervising reviewer defined the training safety boundary and confirmed the final result. The participant completed the inspection, correction, testing, and documentation. No escalation was needed after the system passed verification.

## Reflection

- **What did I initially suspect?** I first suspected an external power connection because the computer wouldn't stay on.
- **What evidence changed my direction?** Brief fan and power activity showed that the system received power, while the stationary CPU fan pointed toward cooling protection.
- **What would I check sooner next time?** I would observe the exact power and fan sequence during the first controlled reproduction.
- **What did I learn?** A short power-on followed by shutdown carries more diagnostic information than a complete no-power symptom.
- **What technical wording would I improve?** I would say "protective shutdown associated with missing CPU fan operation" until the connection and post-fix tests establish the cause.

## Interview-ready answer

In a supervised hardware simulation, I handled a desktop that started briefly and shut down. I verified external power, watched the startup sequence, and saw that the CPU fan wasn't moving. After powering down and following static-safety steps, I found and reconnected the fan lead. I verified two cold starts, normal fan status, and a complete boot. The case taught me to use the timing and physical signs of a failure to narrow the theory safely.

## Evidence

The [evidence guide](evidence/README.md) lists safe artifacts that could support this case. The demo includes no fabricated screenshot or instructor setup detail.

## Sanitization confirmation

- [x] No real requester, participant, account, ticket, device, or organization identifier appears.
- [x] No address, asset tag, serial number, credential, or internal link appears.
- [x] The report describes the learner's troubleshooting experience and excludes condition-staging or reset instructions.
- [x] No screenshot was fabricated.
- [x] The entry is labeled as an illustrative supervised simulation.
- [x] The entry was reviewed against the [Sanitization Guide](../../docs/SANITIZATION-GUIDE.md).
