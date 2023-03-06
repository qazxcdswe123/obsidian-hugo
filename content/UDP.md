---
aliases: [User Datagram Protocol]
tags: []
date created: Feb 20th, 2023
date modified: Feb 20th, 2023
---
- [[TCP]]
- [[ICMP]]
![image.png](https://img.ynchen.me/2023/02/0984bdedbc323ecd40f88f4cecc36af9.webp)
- The UDP datagram is encapsulated in the [[IP]] datagram and sent
- [[Checksum]] is optional when using ipv4
	- Default: All 0s
	- Include part of the [[IP]] headers, allowing detect datagram delivered to the wrong destination.
 - Self contained datagrams
 - Connectionless
 - Unreliable delivery