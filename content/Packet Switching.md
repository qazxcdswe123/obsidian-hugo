---
aliases: []
date created: Mar 5th, 2023
date modified: Mar 8th, 2023
---

# [[Packet]] Switching

## Overview
Time: $\Sigma(\frac{l}{c} + \frac{b}{B} + Q(t))$  
Q is the queueing delay.  
To fight with the random delay, we use buffer to mitigate this impact.

## [[Packet]] Routing
Independently for each arriving [[packet]], pick its outgoing link. If the link is free, send it. Else hold the [[packet]] for later.  
Use **longest prefix match** and forwarding table to route packets (LPM). You need a exact match so any different will be dropped and sent to default route (`0.0.0.0/0`).

The default route in [Internet Protocol Version 4](https://en.wikipedia.org/wiki/IPv4 "IPv4") (IPv4) is designated as the zero address, _0.0.0.0/0_ in [CIDR notation](https://en.wikipedia.org/wiki/CIDR_notation "CIDR notation"). Similarly, in [IPv6](https://en.wikipedia.org/wiki/IPv6 "IPv6"), the default route is specified by _::/0_. The subnet mask is specified as _/0_, which effectively specifies all networks and is the shortest match possible. A route lookup that does not match any other rule falls back to this route.

Each [[packet]] in connectionless [[packet]] switching includes the following information in its header section:

- Source address
- Destination address
- Total number of packets
- Sequence number (Seq#) for reassembly

![ipv4 packet format](https://img.ynchen.me/2023/02/73004f0566a8d6217aa77143416d12aa.webp)

## Ethernet Switch
1. Examine the header of each arriving frame.
2. If the Ethernet DA is in the forwarding table, forward the frame to the correct output port(s).
3. If the Ethernet DA is not in the table, broadcast the frame to all ports (except the one through which the frame arrived).
4. Entries in the table are learned by examining the Ethernet SA of arriving packets.


