---
aliases: [Address Resolution Protocol]
tags: [] 
date created: Feb 22nd, 2023
date modified: Feb 26th, 2023
---
**ARP** stands for “Address Resolution Protocol”, is a protocol for mapping an IP address to a physical MAC address on a local area network.  
any local communications would use MAC address, not IP address.

1. The client sends a broadcast message because the destination MAC address is a broadcast address. Simply saying hello! anyone has IP address 192.168.0.10 if you hear me would you please give me your MAC address?, and here is my IP address and MAC address. Other devices hear the broadcast message and discard the ARP packet silently.
2. When a server hears the message, it sends a unicast message to the client because the destination MAC address and IP address belong to the client.
3. The client cache the servers MAC address. At the same time, the client updates its cache table for future reference.

### ARP Summary
- It is a layer 2 protocol that uses a layer 3 IP address to find layer 2 MAC address.
- It operates on a LAN or the same broadcast domain because ARP relies on broadcasting.
- It uses the ARP table.

## ARP Format
![image.png](https://img.ynchen.me/2023/02/0f799b80e8983ee701cc4bfc0494f40e.webp)
