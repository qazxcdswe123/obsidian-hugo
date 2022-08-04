---
tags: [] 
aliases: [heap]
date created: Jul 17th, 2022
date modified: Jul 28th, 2022
---

[科普 那些放在不同位置的字符串 - 0xFFFF](https://0xffff.one/d/399-ke-pu-nei-xie-fang-zai-bu-tong-wei-zhi-de-zi-fu-chuan)  
[[Stack]]
## Segmentation
[Memory segmentation - Wikipedia](https://en.wikipedia.org/wiki/Memory_segmentation)
[Data segment - Wikipedia](https://en.wikipedia.org/wiki/Data_segment)
[Code segment - Wikipedia](https://en.wikipedia.org/wiki/Code_segment)
[.bss - Wikipedia](https://en.wikipedia.org/wiki/.bss)


## Virtual Memory
Each [[process]] has the same uniform view of memory, which is known as its virtual address space.  
In [[Linux]], the topmost region of the address space is reserved for code and data in the [[operating system]] that is common to all processes. The lower region of the address space holds the code and data defined by the user's [[process]].

![](https://i.stack.imgur.com/HOY4C.png)
[memory management - Stack and Heap locations in RAM - Stack Overflow](https://stackoverflow.com/questions/32418750/stack-and-heap-locations-in-ram)


## Memory Access Rules in [[Assembly]]
Used by [[Instruction]] like `move` or `add`
![](https://img.ynchen.me/2022/07/98f1002e2a47f479253df114d3870376.png)
