# Restore Browser Access After Layered Connectivity Checks

> **Illustrative demo:** This supervised example shows how evidence can disprove an initial theory. It doesn't claim participant experience.

## Context

- **Experience type:** Supervised Windows troubleshooting simulation
- **Date:** Illustrative demo date
- **My role:** Acting support technician responsible for isolation, approved correction, and verification
- **Technical areas:** Windows networking, DNS, proxy settings, command line

## Problem or goal

A user reported that “the internet was down” because websites wouldn't load. The problem affected one Windows workstation. The goal was to separate adapter state, addressing, gateway reachability, name resolution, proxy behavior, and local overrides before making a change.

## Decision record

| Check or action | Why I chose it | What I found | What changed next |
|---|---|---|---|
| Check adapter and IP configuration | Confirm the workstation had a plausible local network state | The adapter was enabled with expected addressing, gateway, and DNS settings | Test reachability |
| Test a known endpoint and default gateway | Separate local link or route failure from higher-layer behavior | Both tests succeeded | Check name resolution |
| Query an approved example name | DNS failure was my leading theory | The query returned a valid documentation address | Reject DNS as the supported cause and inspect the browser traffic path |
| Review proxy and hosts-file settings | These settings can redirect browser requests after DNS succeeds | The hosts file had no relevant override; a stale manual proxy was enabled | Remove the approved stale proxy setting |
| Load two approved example sites | Verify the reported function across more than one destination | Both sites loaded and DNS still worked | Record the correction and result |

## Result and verification

- **Cause:** A stale manual proxy redirected browser traffic to an unavailable path.
- **Correction:** I removed the proxy setting with approval.
- **Verification:** Two approved sites loaded, name resolution remained successful, and the adapter stayed connected.
- **Closing communication:** The user-facing update explained that the browser path had been corrected and asked for a new report if the symptom returned.
- **Remaining limitation:** The exercise didn't measure long-term or application-specific behavior.

## My contribution

In this demo response, the participant tested each layer, rejected the DNS theory when evidence didn't support it, inspected local traffic settings, made the approved change, and verified browser access. No infrastructure change or hidden staging method was involved in the write-up.

## What I learned

- **First theory:** DNS seemed plausible because websites failed by name.
- **Changed direction:** Successful name queries showed that DNS wasn't the failing layer.
- **Next time:** I would ask whether all applications fail or only browser traffic at the beginning.

## Interview answer

In a supervised Windows exercise, websites failed on one workstation. I confirmed the adapter, addressing, gateway path, and DNS before changing anything. When DNS succeeded, I checked browser traffic settings and found a stale manual proxy. I removed it with approval and verified two sites loaded, which taught me to define the failing layer before choosing a correction.

## Evidence

- [Evidence guide](evidence/README.md), which lists safe command and settings artifacts

## Sanitization note

This entry uses approved example destinations and contains no real addresses, names, ticket links, credentials, or deployment instructions.
