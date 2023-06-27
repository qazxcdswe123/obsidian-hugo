---
aliases: [Maximum Transmission Unit]
date created: Apr 4th, 2023
date modified: Apr 4th, 2023
---
The MTU is the maximum payload length for a particular transmission media. For example, the MTU for [[Ethernet]] is typically 1500 bytes. The maximum [[packet]] length for Ethernet is typically 1518 bytes, but that includes 14 bytes of Ethernet header and 4 bytes of [[CRC]], leaving 1500 bytes of payload.
When a [[VLAN]] tag is involved the packet length is increased to 1522 bytes.

## Links
- [Wireshark MTU](https://wiki.wireshark.org/MTU.md)