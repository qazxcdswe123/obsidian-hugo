---
aliases: []
date created: Mar 20th, 2023
date modified: Mar 20th, 2023
---
First sort, then merge, like a [[Merge Sort]].  
IO: $2N * (1 + \lceil log_{2}^{N} \rceil)$  
Sort in input buffer, write it to output buffer. When output buffer is full, write it to disk.
- Optimizations:
	- Rather than just sorting individual pages, let’s load B pages and sort them all at once into a single sorted run.
	- Merge more than 2 sorted runs together at a time.  
![image.png](https://img.ynchen.me/2023/03/5f36014a0e7461da166943c15975d9e0.webp)
