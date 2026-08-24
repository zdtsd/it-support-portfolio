# Browser could not load websites despite an active network link

> **Starter example - not participant work.** This fictionalized troubleshooting example demonstrates how evidence can disprove an initial theory. It contains no internal addresses, names, or deployment instructions.

## Experience type

Sanitized supervised troubleshooting example

## Date

Not applicable - starter example

## Role

Tier 1 technician responsible for separating local connectivity, addressing, name resolution, proxy, browser, and hosts-file causes before making an approved change.

## Technical areas

- Windows network troubleshooting
- DNS and browser connectivity
- Proxy and hosts-file configuration
- Command-line evidence

## Tools used

- Network Connections and adapter status
- `ipconfig`, `ping`, and `nslookup`
- Windows proxy settings
- PowerShell hosts-file review
- Browser functional testing

## User report

The user described the problem as “the internet is down” because websites would not load in the browser. The report didn't establish whether the failure affected the network adapter, IP configuration, routing, DNS, proxy, hosts file, browser, or only one destination.

## Scope and environment

One Windows workstation was affected in a supervised training exercise. The investigation used approved public example destinations and didn't change network infrastructure. The technician was permitted to inspect user-level network and browser settings but needed evidence before making a configuration change.

## Initial observations

- **Observed:** The Ethernet adapter showed an active link.
- **Observed:** Browser requests failed across more than one approved website.
- **Initial theory:** DNS failure appeared plausible because the user saw a name-based website failure.
- **Not yet established:** An active link didn't prove valid addressing, routing, DNS, proxy behavior, or browser operation.
- **Safety or permission boundary:** Preserve current settings before changing them and avoid disabling security controls as a diagnostic shortcut.

## Troubleshooting process

| Step | Reason for Checking | Result | Next Decision |
|---|---|---|---|
| Confirm adapter state and link | Start at the local connection layer and avoid application changes when the adapter is down | Adapter was enabled and link was active | Inspect addressing and gateway information |
| Review `ipconfig /all` | Determine whether the workstation had a valid assigned address, gateway, and DNS servers | Configuration was valid for the approved lab network; no automatic private address was present | Test local and routed reachability |
| Ping the configured gateway and an approved reachable endpoint | Separate a basic path failure from name-resolution or application behavior | Both tests succeeded without loss | General IP reachability was working; test DNS directly |
| Query an approved name with `nslookup` | Test DNS independently of the browser | The expected public example name resolved successfully | The initial DNS theory wasn't supported; inspect settings that can redirect browser traffic |
| Review Windows proxy configuration | Determine whether browser traffic was being sent to an unintended intermediary | A stale manual proxy was enabled and referenced a fictional, unavailable example host | Preserve the setting, disable it under the approved scope, and retest |
| Review the hosts file for the affected names | Rule out a local name override before concluding the proxy was the only relevant configuration issue | No entry redirected or blocked the tested names | Retest the browser after the proxy correction |
| Restart the browser and load two approved example sites | Verify that new browser processes used the corrected setting and that success wasn't destination-specific | Both sites loaded normally | Record the root cause and verified result |

## Root cause

A stale manual proxy setting redirected browser traffic to an unavailable proxy host. Adapter state, IP configuration, routed reachability, DNS resolution, and the relevant hosts-file entries were functioning normally. Successful `nslookup` output was the key evidence that moved the investigation away from the initial DNS theory.

## Resolution

The existing proxy setting was recorded, then the stale manual proxy was disabled within the approved user-level scope. No adapter, DNS server, hosts file, firewall, or infrastructure setting was changed.

## Verification

- **Original function tested:** Opened two approved public example websites in a restarted browser.
- **Observed result:** Both sites loaded normally.
- **Related function checked:** DNS still returned expected results and general IP reachability remained available.
- **User or approved-proxy confirmation:** The exercise owner confirmed that normal browser loading was restored.

## Customer-facing closing note

> The workstation had a valid network connection and name resolution was working. I found an outdated manual proxy setting that was redirecting browser traffic to an unavailable service. I removed that stale setting under the approved scope and verified that two approved websites loaded normally after restarting the browser.

## Commands and tools used

| Command or tool | Purpose | Relevant result |
|---|---|---|
| `ipconfig /all` | Inspect addressing, gateway, and DNS configuration | Showed a valid assigned configuration |
| `ping` | Test local gateway and routed IP reachability | Both approved targets responded |
| `nslookup www.example.com` | Test DNS separately from the browser | Returned the expected documentation-domain result |
| Windows proxy settings | Inspect browser traffic redirection | Revealed the stale manual proxy |
| Hosts-file review | Check for local name overrides | Found no relevant redirect or block |

The entry reports only the meaning of the results. It doesn't reproduce private addresses, hostnames, or full command output.

## What I did personally

In this example, the technician established the scope, tested each network layer in a controlled sequence, rejected the DNS theory using direct evidence, preserved and corrected the proxy setting, reviewed the hosts file, retested browser function, and documented the outcome.

## Collaboration or escalation

The exercise owner confirmed that the manual proxy could be disabled within the lab scope. No network or security escalation was required because the evidence established a local user-level configuration issue. An unexpected or policy-managed proxy would instead require escalation before removal.

## Reflection

- **What did I initially suspect?** DNS failure because the visible symptom involved website names.
- **What evidence changed my direction?** Direct name-resolution testing succeeded while the browser still failed.
- **What would I check sooner next time?** After confirming IP reachability and DNS, I would check proxy configuration before changing adapters or DNS settings.
- **What did I learn?** “Internet down” describes the user's symptom. It doesn't identify a diagnostic layer, and browser traffic can fail while link, addressing, routing, and DNS all work.
- **What technical wording would I improve?** I would say “browser traffic was redirected by a stale manual proxy.” The phrase “the internet connection was broken” doesn't identify the failing layer.

## Interview-ready answer

In a supervised Windows troubleshooting example, a user reported that the internet was down because websites wouldn't load. I confirmed the adapter, addressing, gateway path, and DNS independently. When `nslookup` succeeded, I rejected my initial DNS theory and checked browser traffic settings. I found and removed an approved stale manual proxy, then verified two example sites loaded normally. The case taught me to test each network layer and avoid treating browser failure as one undifferentiated problem.

## Evidence

See the [evidence guidance](evidence/README.md). No screenshots or raw command output are fabricated for this starter example.

## Sanitization confirmation

- [x] No real requester, participant, or unrelated person is named.
- [x] No email address, phone number, internal link, or raw ticket number is present.
- [x] No internal IP address, hostname, domain, asset tag, or serial number is present.
- [x] No credential, token, key, certificate, reset value, or secret is present.
- [x] No unreviewed screenshot is included.
- [x] Instructor-only staging, reset, and remote-support implementation details are excluded.
- [x] The entry is clearly labeled as a supervised demo and makes no participant-experience claim.
