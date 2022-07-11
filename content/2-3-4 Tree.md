src: [https://sedgewick.io/talks/#ll-red-black-trees](https://sedgewick.io/talks/#ll-red-black-trees) 
Used in:[[Red Black Tree 红黑树]] [[Left Leaning Red Black Tree 左倾红黑树]]
## Definition
- Node
	- 2-node = 1 key 2 children
	- 3-node = 2 key 3 children
	- 4-node = 3 key 4 children
- Child
	- Left child = less than key.0
	- Middle.0 child = between key.0 and key.1
	- Middle.1 child = between key.1 and key.2
	- Right child = greater than key.2

## Operation
- Search
	- ![](https://s2.loli.net/2022/03/04/PGF36YlVedOAjqE.png)

- Insert
	1. **Search** to bottom for key
	2. If its a 2-node: convert it to 3-node
	3. If its a 3-node: convert it to 4-node.
	4. If its a 4-node: 
		1. move the middle key to parent
		2. split remainder to two 2-node
		3. goto: 2
		- **Problem here, parent may be 4-node**
		- Solution 1: Use the same method to split parent, then continue up the tree if necessary. (Bottom up, like RBTree-FixUp)
		- Solution 2: Split 4-nodes on the way **down**, insert at **bottom**. (Top down)
	- Splitting 4-nodes on the way **down**
		- **Put the middle to the up right**![](https://s2.loli.net/2022/03/04/6Hi7RuP3v1ZobMx.png)
		- 4-node below a 4-node case never happens
		- Bottom node reached is always a 2-node or a 3-node
	1. 4-node below 2-node
		- ![](https://s2.loli.net/2022/03/04/nTHdbOIk7ziUQD1.png)
	1. 4-node below a 3-node
		- ![](https://s2.loli.net/2022/03/04/Vg6PBYzwUQJukOG.png)
## Conclusion
Too complex for implementation
Enhancement: [[Left Leaning Red Black Tree 左倾红黑树]]