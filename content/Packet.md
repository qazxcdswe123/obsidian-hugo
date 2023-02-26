---
aliases: []
tags: []
date created: Feb 20th, 2023
date modified: Feb 23rd, 2023
---

## Packets
- A self-contained unit of data that carries information necessary for it to reach its destination. 
	- Data
	- From
	- To
- Sent via link layer

## Packet Switching
Independently for each arriving packet, pick its outgoing link. If the link is free, send it. Else hold the packet for later.  
Use **longest prefix match** and forwarding table to route packets (LPM). You need a exact match so any different will be dropped and sent to default route (`0.0.0.0/0`).

The default route in [Internet Protocol Version 4](https://en.wikipedia.org/wiki/IPv4 "IPv4") (IPv4) is designated as the zero address, _0.0.0.0/0_ in [CIDR notation](https://en.wikipedia.org/wiki/CIDR_notation "CIDR notation").[[2]](https://en.wikipedia.org/wiki/Default_route#cite_note-rfc4632-2) Similarly, in [IPv6](https://en.wikipedia.org/wiki/IPv6 "IPv6"), the default route is specified by _::/0_. The subnet mask is specified as _/0_, which effectively specifies all networks and is the shortest match possible. A route lookup that does not match any other rule falls back to this route.

Each packet in connectionless packet switching includes the following information in its header section:

- Source address
- Destination address
- Total number of packets
- Sequence number (Seq#) for reassembly