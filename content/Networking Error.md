---
aliases: []
tags: []
date created: Feb 26th, 2023
date modified: Mar 3rd, 2023
---

# Detection
Each layer has its own error detection: the end-to-end principle

## [[Checksum]]
- [[IP]] prepend a [[checksum]]
- [[IP]], [[UDP]], [[TCP]] use one's complement [[checksum]]

## CRC (Cyclic Redundancy Code)
- Ethernet append a CRC
- Good for detection, catch any 2 bits error, odd number of bit error or any burst $\leq$ `c` bits long.

## MAC (Message Authentication Code)
- [[TLS]] append MAC
- Robust to malicious modifications, but not errors

# Handling
- Wireless network error handling?

## Retransmission Strategy

Based on the size of the receiving buffer size.
### Go Back N
If one failed, retransmit the entire [[Networking Flow Control#Sliding Window Algorithm|window]].  

### Selective Repeat
Retransmit only the [[packet]] that is lost.