---
aliases: []
date created: Jun 11th, 2023
date modified: Jun 11th, 2023
---

## What
Redundant Array of Independent Disks  
A data storage virtualization technology that combines multiple physical disk drive components into one or more logical units for the purposes of data redundancy, performance improvement, or both.

## How
When a [[file system]] issues a logical [[IO|I/O]] request to the RAID, the RAID internally must calculate which disk (or disks) to access in order to complete the request, and then issue one or more physical I/Os to do so.

## RAID Levels
- RAID 0 (Striping): 
	- Split data into blocks and written to multiple disks
	- Better [[IO]].
	- No fault tolerance. A disk fails means data loss.
- RAID 1 (Mirroring): 
	- Written identically on two disks
	- Same perf.
	- Maximum fault tolerance.
 - RAID 2:
	 - Uncommon
	 - bit-level striping
	 - complex error correction code instead of parity
	 - cannot serve multiple requests simultaneously
- RIAD 3:
	- Similar to RAID 5, but use byte-level striping and stores parity calculations on dedicated disk.
	- Cannot serve multiple requests simultaneously
- RAID 4:
	- Block-level striping
	- dedicated parity disk
	- requires at least 3 disks and is prone to botlenecks when storing parity bits for each data block on a single drive
 - RAID 5:
	 - Distributes data and parity information across all disks
	 - provides fault tolerance  
	 - improved read performance
	 - slower write perf due to parity calculations
 - RAID 6:
	 - Similar to RAID 5, but is uses two sets of parity information
	 - better fault tolerance in case of 2 simutaneous disk failures
 - RAID 10 (1+0):
	 - Mirroring data across 2 sets of striped disks
	 - Both fault tolerance and improved performance
 - RAID 50 (5+0):
	 - striping data across multiple RAID 5 arrays
	 - improved perf and fault tolerance
  
![image.png](https://img.ynchen.me/2023/06/31e959bfecb0143235c3b6ce886bd5f1.webp)

  
## Links