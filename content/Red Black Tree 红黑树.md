Simpler Version LLRBT [[Left Leaning Red Black Tree 左倾红黑树]]
Evaluated from: [[B-Tree]] [[2-3-4 Tree]]

# Properties
1. The root is black 
2. NULL is black (`leaf || root.parent`)
3. Red node has 2 black child
4. All paths from the node to descendant leaves contain the same number of black nodes

[[Red Black Tree Insert 红黑树插入]]
[[Red Black Tree Deletion 红黑树删除]]





# Misc
## Lemma 13.1
A red-black tree with $n$ internal nodes has height at most $2\lg(n+1)$
***Proof***  [[Mathematical Induction 数学归纳法]]
- Lemma 1: For subtree rooted at node *x*, internal nodes $\geq \space 2^{bh(x)} - 1$
If height is 0, $2^{bh(x)} - 1 = 0$  OK
Else: [[todo]]



![](https://s2.loli.net/2022/03/10/Si6K298XrGQuEp1.png)
