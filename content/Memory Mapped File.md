---
aliases: [mmap]
date created: Apr 25th, 2023
date modified: Apr 25th, 2023
---
## Benefits
The benefit of memory mapping a file is increasing I/O performance, especially when used on large files. For small files, memory-mapped files can result in a waste of [slack space](https://en.wikipedia.org/wiki/Slack_space), as memory maps are always aligned to the page size, which is mostly 4 KiB. Therefore, a 5 KiB file will allocate 8 KiB and thus 3 KiB are wasted.

Accessing memory mapped files is faster than using direct read and write operations for two reasons. 
- Firstly, a [[syscall|system call]] is orders of magnitude slower than a simple change to a program's local memory. 
- Secondly, in most operating systems the memory region mapped actually _is_ the [[Linux Kernel|kernel]]'s [page cache](https://en.wikipedia.org/wiki/Page_cache "Page cache") (file [[cache]]), meaning that no copies need to be created in user space.

## Links
- [Memory-mapped file - Wikipedia](https://en.wikipedia.org/wiki/Memory-mapped_file)