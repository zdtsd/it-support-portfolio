# Windows Command-Line Troubleshooting Decisions

> **Demo training entry.** This completed example shows what a participant's lab report could look like. The activity and results are illustrative, and the entry contains no production data.

## Objective

Choose Windows command-line tools by the question each tool can answer, test file-management commands in a disposable practice folder, and explain each command's limits.

## Experience type

Supervised CompTIA A+ command-line exercise in a controlled training environment.

## Date

Illustrative demo date: 2026-02-02.

## Skills demonstrated

- Selecting diagnostic commands from symptoms
- Separating local configuration, reachability, path, and connection data
- Using basic file-management commands carefully
- Explaining command limits before drawing a conclusion
- Recording results that support the next troubleshooting decision

## Equipment, software, or topology

- Windows training workstation
- Command Prompt
- Documentation-only test destinations
- Disposable local practice folder

## Starting condition

The exercise provided several short support scenarios, including an unreachable website, an unknown IP configuration, a route question, active connection review, and basic file operations. The task was to select the most useful first command and justify the choice.

## Procedure

### Network command decisions

| Command | Question it answers | Safe example | Useful result | Limit to remember |
|---|---|---|---|---|
| `ping` | Can the target answer ICMP echo requests, and what delay or loss is visible? | `ping example.com` | Replies can show basic reachability and round-trip time | A blocked reply doesn't prove the host is offline, and a reply doesn't prove a website works |
| `ipconfig /all` | What address, gateway, DNS, and adapter settings does this workstation have? | `ipconfig /all` | Shows whether the workstation has a plausible local configuration | It doesn't test the route or application |
| `netstat -ano` | Which local ports, listeners, connections, and process IDs are visible? | `netstat -ano` | Connects network activity with local endpoints and process IDs | It doesn't explain where a remote path fails |
| `tracert` | Which routed hops answer on the path toward a destination? | `tracert example.com` | Helps narrow a path or delay question to a portion of the route | Some routers don't return tracing messages, so a timeout needs context |

### File command decisions

| Command | Question or task | Practice action | Safety note |
|---|---|---|---|
| `dir` | What files and folders are in the current location? | List the practice folder before and after each change | Review the path before modifying anything |
| `cd` | How do I move to another working directory? | Enter the disposable practice folder | Use `cd` and `dir` together to confirm location |
| `mkdir` | How do I create a directory? | Create a folder named `command-lab` | Choose a location where creation is permitted |
| `copy` | How do I duplicate a file? | Copy a harmless text sample inside the practice folder | Confirm source and destination before running it |
| `del` | How do I remove a file? | Delete only the copied practice file | Deletion can be difficult to recover, so confirm the full path first |

### Scenario selection

| Scenario | First command | Reason for the choice |
|---|---|---|
| Test basic reachability to a website host | `ping` | It provides a quick ICMP reachability check before deeper path testing |
| Review the workstation's IP configuration | `ipconfig /all` | It displays adapter, gateway, and DNS configuration in one place |
| Review active network connections | `netstat -ano` | It shows connection states, endpoints, and related process IDs |
| Trace the routed path toward a remote host | `tracert` | It lists responding hops in path order |
| List files in a folder | `dir` | It displays the current directory contents |
| Move to another folder | `cd` | It changes the current working directory |
| Create a practice folder | `mkdir` | It creates the requested directory |
| Remove a disposable test copy | `del` | It removes the selected file after the path is confirmed |
| Duplicate a harmless test file | `copy` | It creates a copy at the chosen destination |

## Expected result

Each scenario should map to a command that directly answers the immediate question. File operations should affect only the disposable practice folder.

## Observed result

The completed decision table matched each scenario to an appropriate first command. The practice folder was created, entered, listed, used for a test copy, and returned to its starting state after the copied file was removed.

The network portion also exposed an important limit: a successful `ping` shows an ICMP response. Browser access still depends on name resolution, routing, proxy settings, firewall behavior, and the destination service.

## Verification

- Re-ran `dir` after each file operation and confirmed the expected folder contents.
- Confirmed the original harmless sample remained after the copied file was deleted.
- Reviewed each network command against the specific question it answers.
- Checked that every conclusion stayed within the command's limits.

These checks prove that the file commands changed only the intended practice files and that the command selections follow a symptom-driven troubleshooting sequence.

## Technical explanation

Command-line tools expose different layers of evidence. `ipconfig` describes local configuration. `ping` checks for an ICMP response. `tracert` observes responding routed hops. `netstat` reports local sockets and connections. A technician can combine these views, but no single command establishes complete network or application health.

The same discipline applies to file commands. `cd` and `dir` establish location and visible contents. `mkdir`, `copy`, and `del` change the file system, so path verification comes first.

## Problems encountered

The first draft treated `ping` as proof that a website worked. Reviewing the scope of ICMP evidence showed that this conclusion was too broad.

## Changes or corrections

The final decision guide describes `ping` as a basic reachability test and calls for DNS, route, proxy, and application checks when the symptom involves a browser.

## What I did personally

In this demo response, the participant selected each command, wrote the justification and limitation, carried out the disposable file operations, and documented the verification.

## Evidence

The [evidence guide](evidence/README.md) lists safe artifacts that could support this entry. No command output or screenshot has been fabricated for the demo.

## Reflection

- **What did I initially suspect?** I initially assumed a successful ping would settle a website connectivity question.
- **What evidence changed my direction?** The command's scope showed that it tests ICMP response and doesn't validate browser settings or the web service.
- **What would I check sooner next time?** I would define the exact failing layer before selecting a command.
- **What did I learn?** A useful command is one that answers the next decision question with the least risk.
- **What technical wording would I improve?** I would describe the observed layer, such as "the host answered ICMP," and avoid saying "the internet works."

## Interview-ready answer

In a supervised command-line exercise, I matched Windows tools to the questions they could answer. I used `ipconfig` for local configuration, `ping` for ICMP reachability, `tracert` for routed hops, and `netstat` for local connections. I also tested file commands in a disposable folder and verified each change with `dir`. The main lesson was to keep conclusions within the limits of the command output.

## Sanitization confirmation

- [x] The entry is labeled as an illustrative training demo.
- [x] No real account, host, address, ticket, or organization detail appears.
- [x] No raw terminal output or unrelated screen content was included.
- [x] Commands with destructive potential are limited to a disposable practice file.
- [x] The entry was reviewed against the [Sanitization Guide](../../docs/SANITIZATION-GUIDE.md).
