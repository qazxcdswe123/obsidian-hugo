---
tags: [] 
aliases: [heap]
date created: Jul 17th, 2022
date modified: Jan 11th, 2023
---
- [科普 那些放在不同位置的字符串 - 0xFFFF](https://0xffff.one/d/399-ke-pu-nei-xie-fang-zai-bu-tong-wei-zhi-de-zi-fu-chuan)  
- [[Stack]]
- [[Virtual Memory]]

## Segmentations
- [Memory segmentation - Wikipedia](https://en.wikipedia.org/wiki/Memory_segmentation)  
- [Data segment - Wikipedia](https://en.wikipedia.org/wiki/Data_segment)  
- [Code segment - Wikipedia](https://en.wikipedia.org/wiki/Code_segment)  
- [.bss - Wikipedia](https://en.wikipedia.org/wiki/.bss)

## Memory Access Rules in [[Assembly Code]]
Used by [[CPU Instruction]] like `move` or `add`  
![](https://img.ynchen.me/2022/07/98f1002e2a47f479253df114d3870376.png)

## Copy on Write
>  If a resource is duplicated but not modified, it is not necessary to create a new resource; the resource can be shared between the copy and the original. Modifications must still create a copy, hence the technique: the copy operation is deferred until the first write. By sharing resources in this way, it is possible to significantly reduce the resource consumption of unmodified copies, while adding a small overhead to resource-modifying operations. —Wikipedia

- [Copy-on-write - Wikipedia](https://en.wikipedia.org/wiki/Copy-on-write)

## Memory Management
- Used in [[Operating System|OS]]

### Free List
- [Free list - Wikipedia](https://en.wikipedia.org/wiki/Free_list)  
Use linked list, when we need to allocate memory we simply move the head to next and use the head, when we free the memory we insert it back to head.

### Base and Bonds