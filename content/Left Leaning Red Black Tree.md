---
aliases: [左倾红黑树]
tags: []
date created: Aug 19th, 2022
date modified: Aug 19th, 2022
---
[Jaca Code](https://algs4.cs.princeton.edu/33balanced/RedBlackBST.java.html)
# Properties
1. Represent [[2-3-4 Tree]] as a [[Binary Tree]].
2. Use "internal" red edges for 3- and 4- nodes.
3. **Require that 3-nodes be left-leaning.**  
![](https://s2.loli.net/2022/03/04/SMK1gojCGIHEF3w.png)
- **Disallowed**
	1. right-leaning 3-node representation  
		![](https://s2.loli.net/2022/03/04/6P7ZHlJM21XSRUv.png)
	2. two reds in a row  
	![](https://s2.loli.net/2022/03/04/SeYwWquv2XTVs1k.png)

# How to
1. In Red-Black Tree, we only rotate red links (to maintain perfect black-link balance)
	- Left Rotate 
		- ![](https://s2.loli.net/2022/03/12/aQPBSC9iKdZA2yW.png)
	- Right Rotate
		- ![](https://s2.loli.net/2022/03/12/pWPHhsA2cFSYkXn.png)
2. Then we maintain preperties
	- Color flip to split 4-node
		- ![](https://s2.loli.net/2022/03/12/LD1sugjIW65QhGm.png)
		- ![](https://s2.loli.net/2022/03/12/tb4AMlZeNJ8QkRI.png)
		- ![](https://s2.loli.net/2022/03/12/ip1lU2xfDZkXcwz.png)
	- left-rotate any right-leaning link on search path
	- right-rotate top link if two reds in a row found
	- trivial with recursion (do it after recursive calls)
	- no corrections needed elsewhere
3. Insert
	1. At the bottom  
		![](https://s2.loli.net/2022/03/12/AZkF6uBQ79rfVwd.png)
	2. Split a 4-node  
		![](https://s2.loli.net/2022/03/12/Q79AHyJeEWGKODN.png)
	3. Enforce left-leaning condition  
		![](https://s2.loli.net/2022/03/12/O8MemyKpVvP1BF4.png)
	4. Balance a 4-node  
		![](https://s2.loli.net/2022/03/12/hdn5v9HJpxOZ42u.png)
	5. Complete Code (A top-down 2-3-4 nodes tree)  
		![](https://s2.loli.net/2022/03/12/ZKJHCXQ2ENF1ez8.png)
	6. If we move the color-flipping precedure to the bottom, it becomes a bottom-up 2-3 nodes tree

# Criticism
[LLRB is BAD](https://www.read.seas.harvard.edu/~kohler/notes/llrb.html)
## Tricky Writing
Sedgewick’s paper is tricky. As of 2013, the insert section presents 2–3–4 trees as the default and describes 2–3 trees as a variant. The delete implementation, however, _only works for 2–3 trees_. If you implement the default variant of insert and the only variant of delete, your tree won’t work. The text doesn’t highlight the switch from 2–3–4 to 2–3: not kind.