---
aliases: []
date created: May 16th, 2023
date modified: Jun 23rd, 2023
---
The Internet Group Management Protocol (IGMP) is a protocol that allows several devices to share one IP address so they can all receive the same data. IGMP is a [[network layer]] 3 protocol used to set up [[Multicast|multicasting]] on networks that use the IPv4. Specifically, IGMP allows devices to join a multicasting group.

Any network traffic directed at that [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) will reach all devices that share the IP address, instead of just one device.

**IGMP uses IP addresses that are set aside for multicasting.** Multicast IP addresses are in the range between 224.0.0.0 and 239.255.255.255. (In contrast, anycast networks can use any regular IP address.)  
Each multicast group shares one of these IP addresses. When a router receives a series of packets directed at the shared IP address, it will duplicate those packets, sending copies to all members of the multicast group.s to leave a multicast group.

## Messages
- **Membership reports**: Devices send these to a multicast router in order to become a member of a multicast group.
- **"Leave group" messages**: These messages go from a device to a router and allow device
- **General membership queries**: A multicast-capable router sends out these messages to the entire connected network of devices to update multicast group membership for all groups on the network.
- **Group-specific membership queries**: Routers send these messages to a specific multicast group, instead of the entire network.

## Links
- [[Multicast]]