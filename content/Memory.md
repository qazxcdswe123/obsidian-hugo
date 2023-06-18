---
aliases: [heap]
date created: Jul 17th, 2022
date modified: Jun 17th, 2023
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

## RAM
The term random-access memory, or RAM, implies that you can access any part of RAM just as quickly as another. 
While it is generally good to think of RAM in this way, because of hardware/[[Operating System|OS]] features such as the TLB, accessing a particular page of memory may be costly, particularly if that page isn’t currently mapped by your TLB. 
Thus, it is always good to remember the implementation tip: RAM isn’t always RAM. Sometimes randomly accessing your address space, particularly if the number of pages accessed exceeds the TLB coverage, can lead to severe performance penalties.

## Links
- [[Stack]]
- [[Virtual Memory]]
- [[Memory Timing]]
- [[Page Table]]
- [[Memory Mapped File]]
- [[Memory Management]]
- [[TLB]]
- [Edge AI Just Got Faster](https://justine.lol/mmap/)
- [科普 那些放在不同位置的字符串 - 0xFFFF](https://0xffff.one/d/399-ke-pu-nei-xie-fang-zai-bu-tong-wei-zhi-de-zi-fu-chuan)  