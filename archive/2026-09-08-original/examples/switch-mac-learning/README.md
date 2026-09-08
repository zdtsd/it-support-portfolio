# Verify Layer 2 Source-MAC Learning After a Port Move

> **Illustrative demo:** This supervised lab contains no management address, credential, production configuration, or instructor setup method.

## Context

- **Experience type:** Supervised managed-switch lab
- **Date:** Illustrative demo date
- **Objective:** Observe how a switch learns and updates a source-MAC location
- **My role:** Apply the approved basic lab configuration, record observations, and explain the result
- **Equipment or topology:** One managed lab switch and one workstation connected to approved access ports

## Problem or goal

The lab needed to demonstrate dynamic source-MAC learning. Running a table command once would show only one moment, so the procedure included a controlled cable move and a second observation.

## Decision record

| Check or action | Why I chose it | What I found | What changed next |
|---|---|---|---|
| Record the empty starting state for the two access ports | Establish a baseline | The workstation MAC wasn't present on either port | Connect the workstation and generate traffic |
| View the table after traffic on the first port | Confirm initial source learning | The workstation MAC appeared dynamically on the first port | Move the same workstation cable |
| Connect to the second port and generate new traffic | Give the switch a frame with the same source MAC on a new ingress port | Link came up and traffic crossed the second port | View the table again |
| Compare the second table state with the baseline | Verify whether the learned location changed | The same MAC appeared on the second port and no longer used the first as its active location | Document what the movement proved |

## Result and verification

- **Observed result:** The switch learned the workstation source MAC on the first port, then updated the location after traffic arrived on the second port.
- **Verification:** The same recorded MAC appeared dynamically on the expected port after each traffic test.
- **What it proves:** A switch learns a frame's source MAC on the ingress port and can update that learned state when the source moves.
- **Remaining limitation:** The lab didn't test aging timers, security features, trunks, or production behavior.

## My contribution

In this demo response, the participant documented the baseline, applied the approved lab configuration, recorded the example MAC, moved the cable, generated traffic, compared table states, and wrote the Layer 2 explanation.

## What I learned

- **Initial expectation:** I expected link-up alone to create the table entry.
- **Changed direction:** The lab required actual frame traffic before the switch had a source to learn.
- **Next time:** I would include traffic generation as an explicit step after every physical move.

## Interview answer

In a supervised switch lab, I recorded a workstation MAC and observed it learned dynamically on one access port. I moved the cable, generated traffic, and verified the same MAC moved to the new port in the table. That result demonstrated source-MAC learning from the ingress frame. It also showed why a command output needs a controlled change and comparison to become useful evidence.

## Evidence

- [Evidence guide](evidence/README.md), which explains safe table excerpts and topology diagrams

## Sanitization note

This entry contains no management address, credential, real hardware address, production configuration, or condition-staging instruction.
