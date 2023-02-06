---
aliases: [红黑树插入]
tags: []
date created: Mar 23rd, 2022
date modified: Feb 2nd, 2023
---

# Implementation

## Rotation
**Left rotate**: 2 nodes with 3 childrens, childrens have same relative postion, and move underneath nodes from right child to left child. Exchange the 2 nodes.  
![](https://s2.loli.net/2022/03/17/eUDub1xCtgEa4Nl.png)

Pic:  
![](https://s2.loli.net/2022/03/17/v7bPs3Al6CJXRpF.png)

![](https://s2.loli.net/2022/03/17/1cdhUVsznaRpoAB.png)  
3. At most one above is violated.
___
![](https://s2.loli.net/2022/03/17/fG8xQmsp763VuXi.png)  
There are 6 cases, but 3 of them are symmetric(z's parent is a left child or right child)  
Known: *z.p.p* exists 

***Core: Make Root RED***

**Case1: z's uncle y is RED** EZ  
Uncle = parent neighbour  
Known: Both *z.p* and *y* are RED  
Change them BLACK, and color *z.p.p* RED, make *z* two levels up.  
![](https://s2.loli.net/2022/03/18/cGNoWEjYXItrKsS.png)


**Case2 && 3**  
Case 2 can change to 3  
**Case 2: z's uncle y is black and z is right child**  
Use a *LeftRotation* to case 3(From right child to left child)  
![](https://s2.loli.net/2022/03/18/CyevFta85u7TIEQ.png)
 
**Case 3: z's uncle y is black and z is left child**
