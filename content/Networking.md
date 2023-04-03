---
aliases: []
date created: Feb 20th, 2023
date modified: Feb 26th, 2023
---
- [[Communication System]]
- [[ARP]]
- [[Packet]]
- [[Networking Error]]
- [[Latency]]
- [[HTTP]]
- [[VLAN]]
- [[Linux Network]]
- [[Gateway]]
- [[Netmask]]

## End-to-End Principle
- [End-to-End principle](https://en.wikipedia.org/wiki/End-to-end_principle)
- Need two end points' joint effort to make communication correct and complete, relay in middle can only check headers but not data. You need an end-to-end check, such as [[Hashing]] or [[Checksum]] to check data integrity.
- Example:
	- File transfer
	- Bittorrent
	- Link reliability (Wireless vs Wired).

___

# Network Model

## 4 Layer Internet Model
- Application Layer
	- Bi-directional reliable byte stream between two applications, using application-specific semantics (e.g. http, bit-torrent).
- Transport Layer
	- [[TCP]] and [[UDP]]
	- Guarantees correct, in-order delivery of data end-to-end. Controls congestion.
- Network Layer
	- No need to concern how [[Packet|packets]] are sent via link layer
	- Delivers datagrams end-to-end. Best-effort delivery -no guarantees. Must use the Internet Protocol ([[IP]]).
- Link Layer
	- Delivers data over a single link between an end host and router, or between routers  
 ![image.png](https://img.ynchen.me/2023/02/f7969e87e3d75926237be138fb447066.webp)

## 7 Layer OSI Model
![image.png](https://img.ynchen.me/2023/02/b0cb7ea848e7e26ea5e44b6f44893468.webp)

___

- [[Networking Homework 1]]
