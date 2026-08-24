# DHCP DORA Process Analysis

> **Demo training entry.** This completed example models a participant's lab report. It describes a conceptual training exercise and contains no live network capture or internal infrastructure data.

## Objective

Build and explain the DHCP Discover, Offer, Request, and Acknowledge sequence, then state what a completed exchange proves about automatic IPv4 configuration.

## Experience type

Supervised CompTIA A+ networking exercise.

## Date

Illustrative demo date: 2026-02-09.

## Skills demonstrated

- Explaining the DHCP DORA sequence
- Reading a client-server message flow
- Connecting protocol messages with lease state
- Identifying the limits of a conceptual model
- Writing a technical explanation in original language

## Equipment, software, or topology

The conceptual topology contained one new client, one DHCP server, and one local broadcast domain. No production device, management interface, or packet capture was used.

## Starting condition

The client had joined the network and had no usable IPv4 lease. It needed an address, subnet information, default gateway, DNS settings, and a defined lease period from the approved DHCP service.

## Procedure

1. Drew the client and DHCP server as separate endpoints.
2. Placed each DORA message in transmission order.
3. Recorded the sender, receiver, purpose, and resulting decision for each message.
4. Checked that the client accepted one offered configuration.
5. Added the lease binding and renewal concept to the final explanation.

| Step | Direction | Purpose | State after the message |
|---|---|---|---|
| Discover | Client to available DHCP servers | Announce that the client needs configuration and identify the request | Servers can evaluate the request and available address pool |
| Offer | DHCP server to client | Propose an available address, lease time, and network options | The client can evaluate an offered configuration |
| Request | Client to DHCP server | Identify the selected offer and request that configuration | Servers can see which offer the client selected |
| Acknowledge | DHCP server to client | Confirm the lease and configuration options | The client can apply the lease and begin normal IPv4 communication |

## Expected result

The flow should show a client progressing from no lease to an acknowledged lease. The explanation should connect each message with a state change and explain how the server tracks address assignments.

## Observed result

The completed flow placed Discover, Offer, Request, and Acknowledge in the correct order. The final state showed one selected configuration associated with the client for a defined lease period.

## Verification

- Followed the arrows from the client through all four messages and back to the client.
- Confirmed that every message had a sender, receiver, purpose, and resulting state.
- Confirmed that the client selected an offer before the server acknowledged the lease.
- Confirmed that the explanation included lease tracking, renewal, and address-pool control.

The sequence proves that the conceptual client can obtain centrally managed configuration through DHCP. It doesn't prove that a live DHCP service is reachable because this exercise didn't include packet capture or a configured test network.

## Technical explanation

DHCP reduces manual configuration by leasing settings from a managed pool. The client begins without enough information for normal unicast IPv4 communication, so the early exchange can use broadcast delivery. A server offers an available configuration. The client's request identifies its selected offer. The acknowledgment creates the usable lease state.

Unique assignment depends on the server's lease database and address-pool controls. The server reserves or records the selected address for the client and lease period. A conflict can still occur when a device uses an unmanaged static address inside the pool, so sound scope planning remains important.

## Problems encountered

The first flowchart showed only message names. It didn't explain what changed after each message, so it couldn't demonstrate understanding of the lease process.

## Changes or corrections

Added direction, purpose, and resulting state for every message. Added a limitation statement to separate a conceptual protocol model from live network verification.

## What I did personally

In this demo response, the participant created the message sequence, wrote each state explanation, checked the logic, and documented the limits of the exercise.

## Evidence

See the [evidence guide](evidence/README.md) for safe artifacts a participant could add. This repository doesn't contain a fabricated packet capture or screenshot.

## Reflection

- **What did I initially suspect?** I first thought memorizing the DORA names was enough to explain DHCP.
- **What evidence changed my direction?** The flow was incomplete until each message showed a specific decision or state change.
- **What would I check sooner next time?** I would identify the starting and ending client state before drawing the arrows.
- **What did I learn?** DHCP combines discovery, selection, confirmation, and lease tracking to automate client configuration.
- **What technical wording would I improve?** I would say "the server acknowledged a lease" and avoid saying "the server permanently gave the client an address."

## Interview-ready answer

In a supervised networking exercise, I built a DHCP DORA flow and explained what changed at each step. The client discovered available service, received an offer, requested one configuration, and received an acknowledgment that established the lease. I verified the sender, receiver, purpose, and state for every message. The exercise helped me explain how centralized lease tracking supports consistent IPv4 configuration.

## Sanitization confirmation

- [x] The entry uses a conceptual topology with no internal addresses or hostnames.
- [x] No live packet capture, credential, or management interface appears.
- [x] The result is described honestly as an illustrative training exercise.
- [x] The entry was reviewed against the [Sanitization Guide](../../docs/SANITIZATION-GUIDE.md).
