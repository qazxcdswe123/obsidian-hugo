---
aliases: []
tags: []
date created: Nov 3rd, 2022
date modified: Nov 3rd, 2022
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
3. **Left Right Case**
4. **Right Right Case**
5. **Right Left Case**