# Managed switch source-MAC learning and port movement

> **Starter example - not participant work.** This fictionalized supervised lab demonstrates the expected technical explanation. It includes no management address, credential, production configuration, or instructor-only setup method.

## Experience type

Sanitized supervised switching lab example

## Date

Not applicable - starter example

## Objective

Apply a basic approved access-port configuration, observe a workstation source MAC address learned on one switch port, move the workstation cable, and verify that the switch relearns the same source MAC address on the new port.

## Skills demonstrated

- Managed-switch CLI navigation
- Access-port configuration within an approved lab scope
- MAC address table interpretation
- Controlled cabling change and verification
- Layer 2 technical explanation

## Equipment, software, or topology

- One managed lab switch
- One workstation with the locally administered example MAC address `02:00:00:00:00:21`
- Two approved access ports in the same lab VLAN
- Console or approved management session
- One Ethernet patch cable

No production device or addressing information is represented.

## Starting condition

The two selected interfaces were approved for the lab and placed in the same access VLAN. The dynamic MAC address table didn't contain the example workstation MAC before the workstation generated traffic. Existing unrelated switch configuration was outside scope and wasn't copied into the report.

## Procedure

1. Recorded the selected interfaces' starting operational state and access VLAN.
2. Applied the approved lab descriptions and access-port settings without changing unrelated interfaces.
3. Connected the workstation to the first access port and waited for link state to become active.
4. Generated ordinary workstation traffic so the switch would receive a frame sourced from the workstation MAC.
5. Queried the dynamic MAC address table and recorded the learned interface.
6. Moved the same cable and workstation to the second approved access port.
7. Waited for link state, generated traffic again, and queried the same MAC entry.
8. Confirmed that the MAC entry now referenced the second port and no longer referenced the first.

## Expected result

After receiving a frame, the switch should associate the frame's source MAC address with the ingress port. When the same source begins transmitting through another port in the same switching context, the switch should update the dynamic entry to the new ingress port.

## Observed result

The example workstation MAC appeared dynamically on the first access port after traffic was generated. After the cable move and new traffic, the same MAC appeared on the second access port. The table no longer showed the first port as the active location for that MAC.

## Verification

- Confirmed link state on each connected port.
- Filtered the dynamic MAC table for the same sanitized example MAC before and after the move.
- Confirmed the access VLAN remained unchanged.
- Generated traffic after each connection so the switch had a source frame to learn.
- Repeated the final lookup to confirm the entry remained associated with the second port.

## Technical explanation

An Ethernet switch learns from the **source** MAC address of frames arriving on each port. It stores a dynamic mapping between that MAC address and the ingress port, then uses destination MAC lookups to make forwarding decisions.

The port movement showed that the table contains learned state that can change. When the switch received a new frame with the same source MAC on the second port, it updated the mapping. Running the table command shows the current entries. The controlled move and second observation demonstrated Layer 2 source-MAC learning and relearning.

## Problems encountered

The MAC entry didn't appear immediately after the first cable connection because link state alone doesn't create a source-MAC entry. The workstation needed to transmit a frame before the switch had a source address to learn.

## Changes or corrections

The procedure was corrected to include deliberate traffic generation after each cable connection and to verify link state before querying the table. This made the observation repeatable.

## What I did personally

In this example, the participant documented the baseline, applied the approved access-port settings, connected and moved the cable, generated test traffic, filtered and interpreted the MAC table, verified the VLAN and interface states, and wrote the technical explanation.

## Evidence

See the [evidence guidance](evidence/README.md). The starter doesn't include fabricated terminal screenshots or a copied full switch configuration.

## Reflection

- **Most important result:** The same source MAC moved from the first interface to the second after new traffic.
- **What it proved:** The switch learns a dynamic association from the ingress location of source frames and can update it when that location changes.
- **What I would change next time:** Include traffic generation as a planned step immediately after link-up.
- **Concept I can explain:** The difference between physical link state, source-MAC learning, and destination-based forwarding.

## Interview-ready answer

In a supervised managed-switch lab, I configured two approved access ports in the same VLAN and recorded the starting MAC table. I connected a workstation, generated traffic, and verified its source MAC was learned on the first port. I then moved the cable, generated traffic again, and confirmed the switch updated the same MAC to the second port. That demonstrated that Layer 2 switches learn dynamic source-MAC-to-port mappings and relearn them when the source location changes.

## Sanitization confirmation

- [x] Device labels, topology, addresses, and evidence are sanitized.
- [x] No management address, credential, key, certificate, asset identifier, or private infrastructure detail is present.
- [x] No instructor-only deployment, fault-staging, or reset method is included.
- [x] The entry is labeled as a supervised demo and makes no participant-experience claim.
- [x] No fabricated evidence is included.
