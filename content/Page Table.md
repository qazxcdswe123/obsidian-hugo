---
aliases: []
tags: []
date created: Jan 11th, 2023
date modified: Feb 20th, 2023
---
Use MMU, Memory Management Unit to translate the address.

## Overview
1. MMU itself will not store page table, it will lookup page table in memory, it will use [TLB](https://en.wikipedia.org/wiki/Translation_lookaside_buffer) as a cache.

## Page
A typical size of page is 4kb (4096 bytes, $2^{12}$ bytes)  
For the [[virtual memory]] address, we split it into 2 parts, `index` and `offset`, `index` for page and `offset` for byte in page, so the size of `offset` is 12 bits, and `index` is 3 `9bit` numbers (L2, L1, L0) in RISC-V. Each memory access need 3 memory lookups and it's expensive, so we use TLB to cache recently used address.

## TLB
A **translation lookaside buffer** (**TLB**) is a memory [cache](https://en.wikipedia.org/wiki/CPU_cache "CPU cache") that stores the recent translations of [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory "Virtual memory") to [physical memory](https://en.wikipedia.org/wiki/Physical_memory "Physical memory"). It is used to reduce the time taken to access a user memory location.[1](https://en.wikipedia.org/wiki/Translation_lookaside_buffer#cite_note-ostep-1-1) It can be called an address-translation cache. It is a part of the chip's [memory-management unit](https://en.wikipedia.org/wiki/Memory_management_unit "Memory management unit") (MMU).  
A TLB may reside between the [CPU](https://en.wikipedia.org/wiki/Central_processing_unit "Central processing unit") and the [CPU cache](https://en.wikipedia.org/wiki/CPU_cache "CPU cache"), between CPU cache and the main memory or between the different levels of the multi-level cache. The majority of desktop, laptop, and server processors include one or more TLBs in the memory-management hardware, and it is nearly always present in any processor that utilizes [paged](https://en.wikipedia.org/wiki/Paging "Paging") or [segmented](https://en.wikipedia.org/wiki/Memory_segmentation "Memory segmentation") [virtual memory](https://en.wikipedia.org/wiki/Virtual_memory "Virtual memory").