---
aliases: []
date created: May 30th, 2023
date modified: May 30th, 2023
---

## What
A database architecture that partitions data by key ranges and distributes the data among two or more database instances. Sharding enables horizontal scaling. See [Sharding.](https://www.mongodb.com/docs/manual/sharding/)

splitting and storing a single logical dataset in multiple databases. By dividing a large dataset into smaller, more manageable parts, sharding can help to improve the speed and performance of database queries.

## How
1. Choose a sharding key
	- a field that can be used to distribute data evenly across shards.
2. Create Shards
	- Each shard is a self-contained database that holds a portion of the total dataset.
3. Distribute Data
	- Use the sharding key to distribute data evenly across your shards.
 4. 
 
## Links
- [[Raft]]  
- [MongoDB Manual](https://mongodb.com/docs/manual/sharding/)
- [[DBMS]]