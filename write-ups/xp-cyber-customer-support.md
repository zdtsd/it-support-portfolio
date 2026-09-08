# XP Cyber: Customer Support Crash Course

> **Illustrative adaptation** inspired by [SibaSec's NICE challenge write-up](https://sibasec.com/post/nice-ticketing-system/). The voice and reflection are examples, not a participant's completion record.

**Setting:** XP Cyber / NICE Challenge simulation

## Problem or goal

I worked through a simulated help-desk queue in osTicket. Users needed help with account access, network connectivity, and shared files across Windows and Linux systems.

## What I found

Similar reports had different underlying causes. Some involved network configuration, while others involved account access or file-sharing setup. Treating every request as the same kind of problem would have missed those differences.

## My approach

I used ticket priority to organize the work and compared the reported symptoms with the expected system behavior. Distinguishing connectivity from name resolution helped me narrow the network issues. For shared files, I considered both access permissions and whether the resource was available to the user.

## Result

I addressed the access and connectivity requests and recorded the outcomes in osTicket. My takeaway was to pair a technical correction with a clear explanation of what changed and whether the requested function works.

## Skills in practice

CompTIA A+ and Network+ concepts: service-desk communication, network troubleshooting, and Windows/Linux administration.

<details>
<summary>Framework connections</summary>

These are suggested connections to the example's scope. A participant should keep only those supported by their own work and results.

| Framework | Connection to this example |
| --- | --- |
| [DoD DCWF](../FRAMEWORK-MAPPINGS.md#dod-dcwf-ksa) | **6010:** described issues and outcomes in tickets. **3513:** applied Windows and Linux administration concepts. |
| [NICE v2.0.0](../FRAMEWORK-MAPPINGS.md#nice-framework) | **K0903, S0478:** organized service-desk work and responded to support requests. **K0983:** used networking principles to distinguish connectivity from name-resolution problems. |
| [NCAE-C](../FRAMEWORK-MAPPINGS.md#ncae-c-knowledge-units) | **Network Technology and Protocols:** considered name resolution and shared-file access. **Operating Systems Administration:** worked with access and configuration across Windows and Linux. |

</details>
