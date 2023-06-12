---
aliases: [mmap]
date created: Apr 25th, 2023
date modified: Apr 25th, 2023
---
## Benefits
Accessing memory mapped files is faster than using direct read and write operations for two reasons. 
- Firstly, a [[syscall|system call]] is orders of magnitude slower than a simple change to a program's local memory. 
- Secondly, in most operating systems the memory region mapped actually _is_ the [[Linux Kernel|kernel]]'s [page cache](https://en.wikipedia.org/wiki/Page_cache "Page cache") (file [[cache]]), meaning that no copies need to be created in user space.

## Concepts
It implements demand paging, meaning that file contents are not immediately read from disk and initially use no physical RAM at all. Instead, the actual reads from disk are performed after a specific location is accessed, in a lazy manner.

## Links
- [Memory-mapped file - Wikipedia](https://en.wikipedia.org/wiki/Memory-mapped_file)