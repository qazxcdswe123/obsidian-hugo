---
aliases: [二叉搜索树,BST]
tags: []
date created: Jun 26th, 2022
date modified: Oct 17th, 2022
---
#Data-structure 

## Operation
[Tree traversal - Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)
### Inorder Tree Walk
从左到右扫描  
从大到小输出  
递归到最左边 - 输出 - 递归到右边

### Preorder Tree Walk
从根节点开始输出 - 递归到左边 - 递归到右边

### Postorder Tree Walk
从右到左扫描  
从小到大输出  
递归到最右边 - 输出 - 递归到左边

### Deletion (Basic) | Change Value
关键：递归。  
删除的是 successor 而不是 target  
每次递归时修改递归方向的节点为函数返回值，达到命中的节点修改，没命中的节点不变的效果（末尾返回 root）不更改中间节点。  
Base Case 有两种，一种是没找到 Key，不做修改 （ return root ）；一种是找到了，分三种情况。
- 左节点为空 - 记录右节点 - 连接
- 右节点为空 - 记录左节点 - 连接
- 含 key 的节点为 root ，有两个子节点，找和它最接近的值（右的最左或左的最右 | successor），修改 root 的值为 successor 的值，删除 successor
