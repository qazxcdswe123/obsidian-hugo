---
aliases: []
date created: Apr 3rd, 2023
date modified: Apr 3rd, 2023
---
## What
- [Banker's algorithm - Wikipedia](https://en.wikipedia.org/wiki/Banker%27s_algorithm)
- A resource allocation and deadlock avoidance algorithm developed by Edsger Dijkstra
- Idea: First give resources to those need less resources, like a [[Greedy]] [[algorithm]].

- We need to know the **available resources, resources needed and available**.
- If safe, we give, then recycle the resources from the finished process.

## How
1. Ask the maximum resources they will need.
2. Then, when a client requests resources, the bank tentatively grants this. 
3. It then checks to see if, after this grant, it can still fulfill the maximum potential request from all clients. 
	1. If it can, it permanently grants the request. 
	2. If it can't, it refuses the request and waits until more resources become available.
4. By doing this, the bank ensures that it never enters a state where it can't fulfill all its commitments, avoiding deadlock situations.