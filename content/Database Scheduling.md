---
aliases: [Database Concurrency]
date created: Jun 8th, 2023
date modified: Jun 21st, 2023
---

## Serializability
Serializability ensures that a schedule (i.e., the sequence of read/write operations) of multiple concurrent transactions is equivalent to some serial execution of those transactions.  
Major correctness criterion for concurrent transactions' executions and is considered the highest level of isolation between transactions

### Conflict Serializability 
If it can be transformed (swapped) into a serial schedule by swapping non-conflicting operations

### View Serializability
View equivalent to some serial schedule, meaning the outcome of the schedule is the same as if the transactions were executed one after another

## Links
- [[Locks]]
- [[Concurrency]]
- [[Database MVCC]]
- [[Database Isolation Level]]
- [[Database Errors]]