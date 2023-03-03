---
aliases: []
tags: []
date created: Feb 26th, 2023
date modified: Feb 26th, 2023
---

# Detection
Each layer has its own error detection: the end-to-end principle

## [[Checksum]]
- [[IP]] prepend a [[checksum]]
- [[IP]], [[UDP]], [[TCP]] use one's complement [[checksum]]

## CRC (Cyclic Redundancy Code)
- Ethernet append a CRC
- Good for detection, catch any 2 bits error, odd number of bit error or any burst $\leq$ `c` bits long.

## MAC (Message authentication Code)
- [[TLS]] append MAC
- Robust to malicious modifications, but not errors

# Handling
- Wireless