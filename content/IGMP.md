> IGMP stands for Internet Group Management Protocol. It is a communication protocol used by hosts and adjacent routers on IPv4 networks to establish [[multicast]] group memberships. IGMP allows several devices to share one IP address so they can all receive the same data. It is an integral part of IP multicast and allows the network to direct multicast transmissions only to hosts that have requested them. 
> IGMP can be used for one-to-many networking applications such as online streaming video and gaming, and allows more efficient use of resources when supporting these types of applications. There are three versions of IGMP: IGMPv1, IGMPv2, and IGMPv3. IGMP is used on IPv4 networks, while multicast management on IPv6 networks is handled by Multicast Listener Discovery (MLD) which is a part of ICMPv6 in contrast to IGMP's bare IP encapsulation.

Any network traffic directed at that [IP address](https://www.cloudflare.com/learning/dns/glossary/what-is-my-ip-address/) will reach all devices that share the IP address, instead of just one device.

IGMP uses IP addresses that are set aside for multicasting. Multicast IP addresses are in the range between 224.0.0.0 and 239.255.255.255. (In contrast, anycast networks can use any regular IP address.)
Each multicast group shares one of these IP addresses. When a router receives a series of packets directed at the shared IP address, it will duplicate those packets, sending copies to all members of the multicast group.

## Links
- [[Multicast]]