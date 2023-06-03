---
aliases: []
date created: Feb 26th, 2023
date modified: Feb 26th, 2023
---
## General Idea
- Don't send more packets than receiver can process
- Receiver gives sender feedback

## Stop and Wait
- A [[State Machine|FSM]]
- At most one [[packet]] inflight at any time
- Sender sends one [[packet]]
- Receiver sends acknowledgment [[packet]] when it receives data
- On receiving acknowledgment, sender sends new data
- On timeout, sender resends current data
- Have trouble when `ACK Delay`, need to use 1-bit counter to detect duplicates

## Sliding Window [[Algorithm]]
- Idea: allow multiple packets, referred to as the window, to be sent without waiting for an acknowledgment (ACK) for each packet.
- [TCP flow control and the sliding window - IBM Documentation](https://www.ibm.com/docs/en/spectrum-protect/8.1.8?topic=tuning-tcp-flow-control)
- Used in [[TCP]]
- Types
	- Stop-and-wait: The simplest sliding window protocol, where the sender sends one packet and waits for the receiver’s acknowledgment before sending the next packet.
	- Go-Back-N: The sender can send multiple packets without waiting for acknowledgments, but has to retransmit all packets from the last unacknowledged one if an error occurs.
	- Selective Repeat: The sender can send multiple packets without waiting for acknowledgments, but only has to retransmit the packets that were lost or corrupted.
	- Sliding-window Network Coding: A variation of Network Coding that improves the throughput of TCP on wireless networks by encoding packets at intermediate nodes and decoding them at the destination.