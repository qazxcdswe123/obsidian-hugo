---
aliases: [heap]
---
- Relationship between stack and heap
> In a multi-threaded application, each thread will have its own stack. But, all the different threads will share the heap. Because the different threads share the heap in a multi-threaded application, this also means that there has to be some coordination between the threads so that they don’t try to access and manipulate the same piece(s) of memory in the heap at the same time.

[[Stack]]

## Memory Access in [[Assembly]]
![](https://img.ynchen.me/2022/07/98f1002e2a47f479253df114d3870376.png)
