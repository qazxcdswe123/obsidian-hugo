---
aliases: [二叉搜索树]
tags: []
date created: Jun 26th, 2022
date modified: Aug 19th, 2022
---
#Data-structure 
- Definition
	- successor
		- 大一位的元素
	- predecessor
		- 小一位的元素

- General
	- 左子树比 root 小，右子树比 root 大

- Operation
	- Inorder Tree Walk
		- 从左到右扫描
		- 从大到小输出
		- 递归到最左边 - 输出 - 递归到右边
	- Preorder Tree Walk
		- 从根节点开始输出 - 递归到左边 - 递归到右边
	- Postorder Tree Walk
		- 从右到左扫描
		- 从小到大输出
		- 递归到最右边 - 输出 - 递归到左边
	- Deletion (Basic) | change value
		- 关键：递归。
		- 删除的是 successor 而不是 target
		- 每次递归时修改递归方向的节点为函数返回值，达到命中的节点修改，没命中的节点不变的效果（末尾返回 root）不更改中间节点。
		- Base Case 有两种，一种是没找到 Key，不做修改 （ return root ）；一种是找到了，分三种情况。
			- 左节点为空 - 记录右节点 - 连接
			- 右节点为空 - 记录左节点 - 连接
			- 含 key 的节点为 root ，有两个子节点，找和它最接近的值（右的最左或左的最右 | successor），修改 root 的值为 successor 的值，删除 successor
	- Deletion (Advanced) | change memory
		- 关键: 分类讨论, 三种情况
		1. target 无 children: 直接删除
		2. target 有一个 children: 更改 `children.parent = target.parent`
		3. target 两个 children
			- Pre-requirement: Transplant
			
			```
			Transplant(T, u, v) // change u with v
			{
				if u.p == NIL;
					T.root = v
				elseif u == u.p.left // u is a left child
					u.p.left = v
				elseif u == u.p.right // u is a right child
					u.p.right = v

				if v != NIL // questionable 
					v.p = u.p // change parent
			} // free memory if needed
			```
			
			2. 找到 successor (在 target 右子树)
			3. 如果 `successor.parent` 就是 target, transplant 之后拼接即可