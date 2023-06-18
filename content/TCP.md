---
aliases: [Transmission Control Protocol]
date created: Feb 20th, 2023
date modified: Mar 5th, 2023
---

## Overview
- **Stream of bytes**
- In sequence
- [[Congestion Control]] (BBR)
- [[Networking Flow Control]] [[Algorithm]] to stop the overflow at the receiver's end
- Provides reliable, ordered, and error-checked delivery of a stream of bytes.

> [[IP]] is a connectionless protocol, which means that each unit of data is individually addressed and routed from the source device to the target device, and the target does not send an acknowledgement back to the source.
> That’s where protocols such as TCP come in. TCP is used in conjunction with IP in order to maintain a connection between the sender and the target and to ensure [[packet]] order.

## 3-way Handshake

### Setup
1. C2S: "Synchronize", "SYN" with sequence number $S_A$ . We do this rather than assume 0 for [[security]] and reliability reason (no overlay window).
2. S2C: "Synchronize and Acknowledge", "SYN/ACK". "SYN" with a sequence number $S_P$ and set the "ACK" bit to 1, ACK $S_{A} + 1$. which indicate the passive side has acknowledged that it received the "SYN"
3. C2S: "Acknowledge", "ACK" $S_{P} + 1$. Send a 0-length $S_{A} + 1$.

### Connection Teardown
1. `A -> A`: FIN, seq $S_A$, ACK $S_B$
2. `B -> A`: (Data+) ACK $S_{A} + 1$, continue sending unfinished packets
3. `B -> A`: FIN, seq $S_B$, ACK $S_{A} + 1$
4. `A - > B`: ACK $S_{B} + 1$

- Problems with closed [[socket]]
	- What if final ack is lost in the network?
	- What if the same port pair is immediately reused for a new connection? 
- Solution:“active” closer goes into TIME WAIT 
	- Active close is sending FIN before receiving one
	- Keep socket around for 2MSL (twice the “maximum segment lifetime") 
- Can pose problems with servers
	- [[Operating System|OS]] has too many sockets in `TIMEWAIT`, slows things down
	- Hack: Can send RST and delete socket, set SO_LINGER socket option to time O
	- [[Operating System|OS]] won't let you re-start server because port still in use (`SO_REUSEADDR` option lets you re-bind used port number)

- TCP [[State Machine|FSM]]
![image.png](https://img.ynchen.me/2023/03/e68394c838122d41d6df2230509a5c00.webp)


## Header
![image.png](https://img.ynchen.me/2023/02/ba7176008713663b7783020ea64c8454.webp)


## Links
- [[UDP]]
- [[ICMP]]