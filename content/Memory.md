---
aliases: [heap]
date created: Jul 17th, 2022
date modified: Apr 10th, 2023
---

## Segmentations
- [Memory segmentation - Wikipedia](https://en.wikipedia.org/wiki/Memory_segmentation)  
- [Data segment - Wikipedia](https://en.wikipedia.org/wiki/Data_segment)  
- [Code segment - Wikipedia](https://en.wikipedia.org/wiki/Code_segment)  
- [.bss - Wikipedia](https://en.wikipedia.org/wiki/.bss)

## Copy on Write
>  If a resource is duplicated but not modified, it is not necessary to create a new resource; the resource can be shared between the copy and the original. Modifications must still create a copy, hence the technique: the copy operation is deferred until the first write. By sharing resources in this way, it is possible to significantly reduce the resource consumption of unmodified copies, while adding a small overhead to resource-modifying operations. —Wikipedia

- [Copy-on-write - Wikipedia](https://en.wikipedia.org/wiki/Copy-on-write)
- [[File System]]

## Memory Management Methods
- Used in [[Operating System|OS]]

### Free List
- [Free list - Wikipedia](https://en.wikipedia.org/wiki/Free_list)  
Use [[linked list]], when we need to allocate memory we simply move the head to next and use the head, when we free the memory we insert it back to head.

## Links
- [科普 那些放在不同位置的字符串 - 0xFFFF](https://0xffff.one/d/399-ke-pu-nei-xie-fang-zai-bu-tong-wei-zhi-de-zi-fu-chuan)  
- [[Stack]]
- [[Virtual Memory]]
- [[Memory Timing]]
- [[Page Table]]
[Edge AI Just Got Faster](https://justine.lol/mmap/)