---
aliases: [Transmission Control Protocol]
tags: [] 
date created: Feb 20th, 2023
date modified: Feb 26th, 2023
---
- [[UDP]]
- [[ICMP]]

## Overview
- **Stream of bytes**
- In sequence
- Congestion Control (BBR)
- [[Flow control]]

## 3-way Handshake
1. C2S: "Synchronize", "SYN"
2. S2C: "Synchronize and Acknowledge", "SYN/ACK"
3. C2S: "Acknowledge", "ACK"


![image.png](https://img.ynchen.me/2023/02/ba7176008713663b7783020ea64c8454.webp)

## Connection Teardown
1. `A -> A`: FIN
2. `B -> A`: (Data+) ACK, continue sending unfinished packets
3. `B -> A`: FIN
4. `A - > B`: ACK