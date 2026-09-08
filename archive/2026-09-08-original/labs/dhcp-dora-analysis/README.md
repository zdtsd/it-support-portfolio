# Explain the DHCP DORA Lease Sequence

> **Illustrative demo:** This conceptual exercise contains no live capture or internal network data.

## Context

- **Experience type:** Supervised networking exercise
- **Date:** Illustrative demo date
- **Objective:** Explain the DHCP Discover, Offer, Request, and Acknowledge sequence
- **My role:** Build the flow, describe each state change, and check the explanation
- **Equipment or topology:** One conceptual client, one DHCP server, and one local broadcast domain

## Problem or goal

The client began without a usable IPv4 lease. The exercise needed to explain how it could obtain an address, network options, and a lease period from an approved DHCP service. Memorizing the four message names wouldn't explain the process by itself.

## Decision record

| Check or action | Why I chose it | What I found | What changed next |
|---|---|---|---|
| Define the client's starting and ending states | Give the message flow a purpose | The client moved from no lease to an acknowledged lease | Place each message between those states |
| Add Discover and Offer | Show service discovery and a proposed configuration | Available servers could see the request and one could offer lease terms | Show how the client selects an offer |
| Add Request | Identify the selected server and configuration | The request told servers which offer the client chose | Confirm the selected lease |
| Add Acknowledge | Establish the usable final state | The server confirmed the lease and options | Add lease tracking and renewal to the explanation |
| Review direction, purpose, and state for every message | Check that the flow explained more than acronyms | Every message had a sender, purpose, and resulting decision | Record the conceptual limit |

## Result and verification

- **Observed result:** The completed flow placed Discover, Offer, Request, and Acknowledge in order.
- **Verification:** Each message had a sender, receiver, purpose, and state change, and the client selected an offer before acknowledgment.
- **What it proves:** DHCP can provide centrally managed IPv4 configuration through a tracked lease process.
- **Remaining limitation:** A conceptual flow can't establish that a live DHCP server is reachable.

## My contribution

In this demo response, the participant created the message sequence, wrote each state explanation, checked the logic, and stated the limit of the exercise.

## What I learned

- **Initial expectation:** I thought knowing the DORA names was enough.
- **Changed direction:** The flow remained incomplete until each message showed a specific decision or state change.
- **Next time:** I would define the starting and ending states before drawing protocol arrows.

## Interview answer

In a supervised networking exercise, I built a DHCP DORA flow and explained what changed at each step. The client discovered service, received an offer, requested one configuration, and received an acknowledgment that established the lease. I verified the sender, purpose, and state for every message. The exercise helped me explain how centralized lease tracking supports consistent IPv4 configuration.

## Evidence

- [Evidence guide](evidence/README.md), which explains safe conceptual diagrams

## Sanitization note

This entry contains no internal addresses, hostnames, hardware addresses, credentials, or packet capture.
