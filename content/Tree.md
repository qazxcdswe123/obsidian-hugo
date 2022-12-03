---
aliases: [树]
tags: []
date created: Jun 26th, 2022
date modified: Nov 23rd, 2022
---
#Data-structure  
[[Graph Theory]]

## Operation
[Tree traversal - Wikipedia](https://en.wikipedia.org/wiki/Tree_traversal)  
![](https://img.ynchen.me/2022/11/149dd8c2dc3e1dc022da82f0cc224260.webp)

### Inorder Tree Walk
从左到右扫描  
从小到大输出  
递归到最左边 - 输出 - 递归到右边  
输出在两个遍历之间  
or use an auxiliary stack [Inorder Tree Traversal without Recursion - GeeksforGeeks](https://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion/) 

```c++
void printInorder(struct Node* node)
{
    if (node == NULL)
        return;
 
    /* first recur on left child */
    printInorder(node->left);
 
    /* then print the data of node */
    cout << node->data << " ";
 
    /* now recur on right child */
    printInorder(node->right);
}
```

### Preorder Tree Walk
从根节点开始输出 - 递归到左边 - 递归到右边  
输出在两个遍历前

### Postorder Tree Walk
从底到上扫描  
递归到最下左边 - 输出 - 递归到下右边  
Postorder traversal is used to delete the tree. Please see [the question for the deletion of a tree](https://www.geeksforgeeks.org/write-a-c-program-to-delete-a-tree/) for details. Postorder traversal is also useful to get the postfix expression of an expression tree  
输出在两个遍历后

- [[Binary Search Tree]]
- [[Threaded Binary Tree]]
- [[B-Tree]]
- [[Red Black Tree]]
- [[AVL Tree]]
- [[Skip List]]