# Websites wouldn't load

> **Fictional example:** This shows the writing style, not a participant's completed work.

**Setting:** Supervised support simulation

## Problem or goal

A user said the internet was down because websites wouldn't open on their Windows computer.

## What I found

An outdated proxy setting was sending browser traffic through an unavailable connection. The computer still had network access.

## My approach

I separated basic network access from the browser's ability to load a website. Successful connection and name-lookup checks made my initial DNS theory less likely and pointed me toward the browser's settings. My instructor confirmed that the old proxy wasn't required, and I corrected that setting.

## Result

I opened two websites that hadn't loaded before. Both worked after the change. This reminded me to test my first idea before assuming it was the cause.

## Skills in practice

CompTIA A+ concepts: network troubleshooting, DNS checks, and proxy settings.

<details>
<summary>Framework connections</summary>

| Framework | Connection to this example |
| --- | --- |
| [DoD DCWF](../FRAMEWORK-MAPPINGS.md#dod-dcwf-ksa) | **22:** used networking concepts to distinguish connectivity, name lookup, and browser behavior. |
| [NICE v2.0.0](../FRAMEWORK-MAPPINGS.md#nice-framework) | **K0983, S0661:** applied networking principles to troubleshoot a client problem. |
| [NCAE-C](../FRAMEWORK-MAPPINGS.md#ncae-c-knowledge-units) | **Basic Networking:** distinguished a network connection from a working application connection. |

</details>
