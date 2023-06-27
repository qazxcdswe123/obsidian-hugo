---
aliases: []
date created: Jun 23rd, 2023
date modified: Jun 23rd, 2023
---

## Leaky Bucket Algorithm
Data always pass in the smae rate

## Token Bucket Algorithm
When a packet (data) needs to be sent, it grabs a token. If there are no tokens, it has to wait. This allows for bursty data, as you could save up tokens when traffic is low and spend them when a burst of data arrives.  
- Like PV [[Semaphore]]

## Links
[Traffic shaping - Wikipedia](https://en.wikipedia.org/wiki/Traffic_shaping)