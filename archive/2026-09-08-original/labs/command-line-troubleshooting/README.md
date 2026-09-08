# Select Windows Commands by the Question They Answer

> **Illustrative demo:** This supervised exercise uses safe example destinations and a disposable practice folder.

## Context

- **Experience type:** Supervised command-line exercise
- **Date:** Illustrative demo date
- **Objective:** Choose Windows commands from troubleshooting questions and explain their limits
- **My role:** Select commands, justify each choice, test safe file actions, and verify the results
- **Equipment or topology:** Windows training workstation and Command Prompt

## Problem or goal

The exercise presented network and file-management scenarios. The goal was to choose the command that answered the immediate question and avoid conclusions broader than the output supported.

## Decision record

| Check or action | Why I chose it | What I found | What changed next |
|---|---|---|---|
| Use `ipconfig /all` for local network state | It shows adapter, address, gateway, and DNS configuration | The command can establish configuration and can't test the full path | Use a connectivity tool for reachability questions |
| Use `ping` for a quick ICMP test | It can show replies, loss, and approximate delay | A reply doesn't prove a website or application works | Use DNS, path, and application checks as the symptom requires |
| Use `tracert` for routed-hop questions | It shows responding hops toward a destination | A timeout may reflect filtering | Interpret timeouts with other evidence |
| Use `netstat -ano` for local connection questions | It shows endpoints, states, and process IDs | It doesn't explain the remote route | Match the output to a local process or service question |
| Test `mkdir`, `cd`, `copy`, `dir`, and `del` in a practice folder | File-changing commands need a safe boundary | The copied test file was created, listed, and removed while the original remained | Verify the path before every file change |

## Result and verification

- **Observed result:** Each scenario was matched with a command that directly addressed the next decision.
- **Verification:** `dir` confirmed every practice-folder change, and the original test file remained after the copy was removed.
- **What it proves:** Command choice should follow the question being asked. No single networking command establishes complete application health.
- **Remaining limitation:** The exercise didn't diagnose a live production incident.

## My contribution

In this demo response, the participant selected and justified each command, described its limits, completed the disposable file operations, and checked the results. No destructive command was used outside the practice folder.

## What I learned

- **Initial expectation:** I first treated a successful `ping` as proof that a website worked.
- **Changed direction:** Reviewing ICMP scope showed that browser access also depends on name resolution, traffic settings, and the destination service.
- **Next time:** I would define the failing layer before choosing the first command.

## Interview answer

In a supervised command-line exercise, I matched Windows tools to the questions they could answer. I used `ipconfig` for local configuration, `ping` for ICMP reachability, `tracert` for routed hops, and `netstat` for local connections. I tested file commands in a disposable folder and verified each change with `dir`. The main lesson was to keep conclusions within the limits of the output.

## Evidence

- [Evidence guide](evidence/README.md), which lists safe command excerpts and decision tables

## Sanitization note

This entry contains no real account, hostname, address, directory path, credential, or raw terminal capture.
