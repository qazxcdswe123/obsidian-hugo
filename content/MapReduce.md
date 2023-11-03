---
aliases: []
link:
  - "[[Hadoop]]"
date created: Aug 9th, 2023
date modified: Aug 10th, 2023
---

## What
A framework (abstraction) for processing and generating large datasets on a [[Distributed System]]

divide and conquer + [[Functional Programming]] + Pipelining

## How

### Map
- Input: kv pair
- Output (`emit`): intermediate kv pair

### Reduce
After all `maps` have finished
- Input: **grouped** intermediate kv pair (need to first **collect** and group before starting)
- Output (`emit`): desired result

### Optimization
- (In the old time) The bottle neck is in network, since [[GFS]] is involved, we can find who hold the input file then have the worker working on it.
- Data streaming
- Use [[Hashtable]] to group intermedia file
- Load balance: Many more tasks than workers

## Abstraction
- MapReduce hides many details:
	- sending app code to servers
	- tracking which tasks are done
	- moving data from Maps to Reduces
	- balancing load over servers
	- recovering from failures
## Links
- [https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf](https://pdos.csail.mit.edu/6.824/papers/mapreduce.pdf)
- [[Hadoop]]