---
aliases: []
tags: []
date created: Nov 1st, 2022
date modified: Nov 2nd, 2022
---
[Threaded Binary Tree - GeeksforGeeks](www.geeksforgeeks.org/threaded-binary-tree/)  
[Threaded binary tree - Wikipedia](https://en.wikipedia.org/wiki/Threaded_binary_tree)
## Idea
The idea of threaded binary trees is to make inorder traversal faster and do it without stack and without recursion. A binary tree is made threaded by making all right child pointers that would normally be NULL point to the inorder successor of the node (if it exists).  
![](https://img.ynchen.me/2022/11/c1bd7d8b509ab1e13d4e3a5dd4cc7e4b.webp)
- _**Single Threaded:**_ Where a NULL right pointers is made to point to the inorder successor (if successor exists)  
- _**Double Threaded:**_ Where both left and right NULL pointers are made to point to inorder predecessor and inorder successor respectively. The predecessor threads are useful for reverse inorder traversal and postorder traversal.  
The threads are also useful for fast accessing ancestors of a node.  
Following diagram shows an example Single Threaded Binary Tree. The dotted lines represent threads.

![](https://img.ynchen.me/2022/11/4c4a14b49651aaf80ffd9b80d66d7c2e.webp)
## Code
