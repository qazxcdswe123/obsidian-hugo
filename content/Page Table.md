---
aliases: []
date created: Jan 11th, 2023
date modified: Jun 4th, 2023
---
Use MMU, Memory Management Unit to translate the address.

## Overview
MMU itself will not store page table, it will lookup page table in memory, it will use [TLB](https://en.wikipedia.org/wiki/Translation_lookaside_buffer) as a cache.

- [[Page]]

## TLB
A **translation lookaside buffer** (**TLB**) is a memory [cache](https://en.wikipedia.org/wiki/CPU_cache "CPU cache") that stores the recent translations of [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory "Virtual memory") to [physical memory](https://en.wikipedia.org/wiki/Physical_memory "Physical memory"). It is used to reduce the time taken to access a user memory location.[1](https://en.wikipedia.org/wiki/Translation_lookaside_buffer#cite_note-ostep-1-1) It can be called an address-translation cache. It is a part of the chip's [memory-management unit](https://en.wikipedia.org/wiki/Memory_management_unit "Memory management unit") (MMU).  
A TLB may reside between the [CPU](https://en.wikipedia.org/wiki/Central_processing_unit "Central processing unit") and the [CPU cache](https://en.wikipedia.org/wiki/CPU_cache "CPU cache"), between CPU cache and the main memory or between the different levels of the multi-level cache. The majority of desktop, laptop, and server processors include one or more TLBs in the memory-management hardware, and it is nearly always present in any processor that utilizes [paged](https://en.wikipedia.org/wiki/Paging "Paging") or [segmented](https://en.wikipedia.org/wiki/Memory_segmentation "Memory segmentation") [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory "Virtual memory").

- [[Page Fault]]
