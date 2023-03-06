---
aliases: []
tags: []
date created: Feb 26th, 2023
date modified: Feb 26th, 2023
---
## General Idea
- Don't send more packets than receiver can process
- Receiver gives sender feedback

## Stop and Wait
- [[State Machine|FSM]]
- At most one [[packet]] inflight at any time
- Sender sends one packet
- Receiver sends acknowledgment [[packet]] when it receives data
- On receiving acknowledgment, sender sends new data
- On timeout, sender resends current data
- Have trouble when `ACK Delay`, need to use 1-bit counter to detect duplicates

## Sliding Window [[Algorithm]]
- Used in [[TCP]]
- Maintain 3 variables
	- Send window size (SWS)
	- Last acknowledgment received (LAR)
	- Last segment sent (LSS)
 - Invariant: (LSS -LAR) $\leq$ SWS
 - Receive Window Size(RWS) $\leq$ SWS
	 - If RWS = 1, 