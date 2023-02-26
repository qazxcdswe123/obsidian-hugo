---
aliases: [B Plus Tree]
tags: []
date created: Feb 22nd, 2023
date modified: Feb 23rd, 2023
---
- “+”? [[B-tree]] that stores data entries in leaves only

- `d`: The order of the tree
	- d <= `#entries` <= 2d
	- max `fan-out`: `2d + 1
	- There are at least two children in the root.
	- `d=2`: 20, nodes;`d=3`: 500 nodes
	- Typical order: 1600
	- Typical fill rate: 67%
- Each interior node is at least partially full:

## Insertion
1. Have enough space
	1. Find the right leaf.
	2. Sort in the leaf.
 2. Do not have enough space
	 1. Split leaf if there is not enough room
	 2. Redistribute entries evenly
	 3. Fix next/prev pointers
	 4. Copy up from leaf the middle key (Left most key in second leaf)
	 5. If no room in parent
		 1. **Recursively** split index nodes
		 2. Redistribute the rightmost d keys to make them split evenly
		 3. Push up middle key (Left most in index node)
		 4. Sort
- **Notice that the leaf key is copied but the index key is pushed**
- Notice that the root was split to increase the height
- Grow from the root not the leaves
- All paths from root to leaves are equal lengths

## Deletion
- In practice, occupancy invariant often not enforced
- Just delete leaf entries and leave space
- If new inserts come, great 
- This is common
- If page becomes completely empty, can delete
- Parent may become underfull
- That’s OK too
- Guarantees still attractive: logF(max size of tree)

## Bulk Loading

## Links
[B+ Tree Visualization](https://www.cs.usfca.edu/~galles/visualization/BPlusTree.html)