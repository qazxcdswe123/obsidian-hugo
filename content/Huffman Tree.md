---
aliases: []
tags: []
date created: Oct 26th, 2022
date modified: Oct 26th, 2022
---
Tags: [[贪心算法|Greedy]]  
The code for A is 0, and no other code starts with 0; the code for T is 11, and no other code starts with 11; and so on. We call such a code a **prefix-free code**.  
Use Priority [[Queue]] to determine which (node or subtree) is the next one to insert.

1. Insert all node in priority queue
2. Extract 2 minimum, make them two child of a subtree, insert them back to priority queue, mark as subtree.
3. While still have node, goto 2