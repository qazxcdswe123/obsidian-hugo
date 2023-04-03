---
aliases: []
date created: Nov 3rd, 2022
date modified: Nov 21st, 2022
---
A Balanced [[Binary Search Tree]]

## Properties
the difference between heights of left and right subtrees cannot be more than one for all nodes

## Insertion

### Rotation
For the unbalanced subtree, we need rotation to make them balanced

```
T1, T2 and T3 are subtrees of the tree, rooted with y (on the left side) or x (on the right side)     
      
     y                               x
    / \     Right Rotation          /  \
   x   T3   - - - - - - - >        T1   y 
  / \       < - - - - - - -            / \
 T1  T2     Left Rotation            T2  T3
 
Keys in both of the above trees follow the following order 
keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
So BST property is not violated anywhere.
```

### The 4 Cases
We define
- `w`: the newly inserted node  
- `z`: the first unbalanced node(from bottom up)  
- `y`: child of `z` (from `w` to `z`)  
- `x`: child of `y`, grandchild of `z` (from w to `z`)  
Now the 4 cases are
- y is the left child of z and x is the left child of y (Left Left Case) 
- y is the left child of z and x is the right child of y (Left Right Case) 
- y is the right child of z and x is the right child of y (Right Right Case) 
- y is the right child of z and x is the left child of y (Right Left Case)

1. **Left Left Case**

```
T1, T2, T3 and T4 are subtrees.
         z                                      y 
        / \                                   /   \
       y   T4      Right Rotate (z)          x      z
      / \          - - - - - - - - ->      /  \    /  \ 
     x   T3                               T1  T2  T3  T4
    / \
  T1   T2
```

2. **Left Right Case**

```
     z                               z                           x
    / \                            /   \                        /  \ 
   y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
  / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
T1   x                          y    T3                    T1  T2 T3  T4
    / \                        / \
  T2   T3                    T1   T2
```

3. **Right Right Case**

```
  z                                y
 /  \                            /   \ 
T1   y     Left Rotate(z)       z      x
    /  \   - - - - - - - ->    / \    / \
   T2   x                     T1  T2 T3  T4
       / \
     T3  T4
```

4. **Right Left Case**

```
   z                            z                            x
  / \                          / \                          /  \ 
T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
    / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
   x   T4                      T2   y                  T1  T2  T3  T4
  / \                              /  \
T2   T3                           T3   T4
```

Approach
> The idea is to use recursive BST insert, after insertion, we get pointers to all ancestors one by one in a bottom-up manner. So we don’t need a parent pointer to travel up. The recursive code itself travels up and visits all the ancestors of the newly inserted node.

- Perform the normal [BST insertion.](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/) 
- The current node must be one of the ancestors of the newly inserted node. Update the **height** of the current node. 
- Get the balance factor **(left subtree height – right subtree height)** of the current node. 
- If the balance factor is greater than **1,** then the current node is unbalanced and we are either in the **Left Left case** or **left Right case**. To check whether it is **left left case** or not, compare the newly inserted key with the key in the **left subtree root**. 
- If the balance factor is less than **-1**, then the current node is unbalanced and we are either in the Right Right case or Right-Left case. To check whether it is the Right Right case or not, compare the newly inserted key with the key in the right subtree root.

## Deletion
1. Perform the normal BST deletion. 
2. The current node must be one of the ancestors of the deleted node. Update the height of the current node. 
3. Get the balance factor (left subtree height – right subtree height) of the current node. 
4. If balance factor is greater than 1, then the current node is unbalanced and we are either in Left Left case or Left Right case. To check whether it is Left Left case or Left Right case, get the balance factor of left subtree. If balance factor of the left subtree is greater than or equal to 0, then it is Left Left case, else Left Right case. 
5. If balance factor is less than -1, then the current node is unbalanced and we are either in Right Right case or Right Left case. To check whether it is Right Right case or Right Left case, get the balance factor of right subtree. If the balance factor of the right subtree is smaller than or equal to 0, then it is Right Right case, else Right Left case.

## Links
[Deletion in an AVL Tree - GeeksforGeeks](https://www.geeksforgeeks.org/deletion-in-an-avl-tree/)
