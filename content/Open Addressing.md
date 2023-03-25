---
aliases: []
tags: []
date created: Nov 23rd, 2022
date modified: Nov 23rd, 2022
---

## What
**Open addressing**, or **closed hashing**, is a method of [collision resolution in hash tables](https://en.wikipedia.org/wiki/Hash_table#Collision_resolution "Hash table"). With this method a hash collision is resolved by **probing**, or searching through alternative locations in the array (the _probe sequence_) until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table. Well-known probe sequences include:
- [Linear probing](https://en.wikipedia.org/wiki/Linear_probing "Linear probing")
	- in which the interval between probes is fixed — often set to 1.
	- **Fastest and simplest** due to its good [locality of reference](https://en.wikipedia.org/wiki/Locality_of_reference "Locality of reference"), but is more sensitive to the quality of its hash function than some other collision resolution schemes.
	- See also [[Cache]]
- [Quadratic probing](https://en.wikipedia.org/wiki/Quadratic_probing "Quadratic probing")
	- in which the interval between probes increases quadratically (hence, the indices are described by a quadratic function).
- [Double hashing](https://en.wikipedia.org/wiki/Double_hashing "Double hashing")  
	- in which the interval between probes is fixed for each record but is computed by another hash function.

## How
Search through alternative locations in the array (the _probe sequence_) until either the target record is found, or an unused array slot is found, which indicates that there is no such key in the table.

## Why
To find the place for items that have the same hash.

## Links
- [Open addressing - Wikipedia](https://en.wikipedia.org/wiki/Open_addressing)
- [[Hashtable]]