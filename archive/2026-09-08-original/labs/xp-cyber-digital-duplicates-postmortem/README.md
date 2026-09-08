# Digital Duplicates: XP Cyber Post-Mortem

> **Illustrative demo:** This sample reflection uses a publicly shared XP Cyber submission report. It does not represent the report owner's words or exact process.

## Context

- **Experience type:** Illustrative supervised cyber-range post-mortem
- **Date:** Illustrative reflection date; source report submitted 2022-02-05
- **Objective:** Preserve original digital evidence, create a forensic duplicate, and evaluate its integrity
- **My role:** Sample participant reflection
- **Evidence:** XP Cyber-generated report with QR-linked verification

## Problem or goal

The exercise involved suspicious removable media that needed preservation for later examination. The goal was to create a forensic image while protecting the original, then compare SHA-512 values to evaluate the image's integrity.

## Decision record

| Check or action | Why I chose it | What I found | What changed next |
|---|---|---|---|
| Protect the original media | Routine access could change evidence | Preservation was the first constraint | Keep acquisition separate from analysis |
| Distinguish source and destination | A selection error could damage evidence | Each had a different purpose | Confirm the boundary before imaging |
| Create the image in the approved workspace | Analysis should use a duplicate | The range accepted the image | Evaluate integrity before relying on it |
| Compare SHA-512 values and review the report | A completed copy alone doesn't establish integrity | The report recorded a full pass and workforce mappings | Document the result without a walkthrough |

## Result and verification

- **Observed result:** The report records 12 minutes and a full pass, 1 of 1, for "Forensic Image Created."
- **Verification:** Its XP Cyber page uses the report UID and submission ID to verify the report.
- **What it proves:** XP Cyber recorded the required outcome for that submission.
- **Remaining limitation:** The report omits digest values and acquisition logs, so it cannot establish every acquisition detail.

### Report-supplied workforce alignment

These historical report mappings are evidence labels rather than self-awarded ratings.

| ID | Area | Connection |
|---|---|---|
| T0048 | Create a forensically sound duplicate | The forensic-image check passed |
| K0118 | Preserve digital evidence | Protection of the original was the primary constraint |
| S0047 | Preserve evidence integrity | The image and integrity comparison support analysis |
| S0089 | Use one-way hash functions | The report identifies SHA-512 as the comparison method |

## My contribution

Sample participant wording: I protected the original evidence boundary, created the required image, evaluated its integrity, and reviewed the generated report. Each participant should replace this with actions they performed and can explain.

## What I learned

- **Initial expectation:** I thought producing a duplicate was the entire objective.
- **Changed direction:** The integrity requirement connected imaging with preservation, verification, and documentation.
- **Next time:** I would prepare an acquisition checklist and approved evidence log first.

## Interview answer

In a supervised cyber-range exercise, I preserved potential evidence by working from a forensic image. I evaluated the image with an integrity comparison, and the XP Cyber report recorded a full pass. I learned that acquisition depends on careful source handling, verification, and documentation.

## Evidence

- [Evidence guide and public reference report](evidence/README.md)

## Sanitization note

This demo reproduces no participant identifier, command, path, screenshot, or range configuration. The source PDF remains in its owner's repository, and the reflection provides no reproducible solution.
