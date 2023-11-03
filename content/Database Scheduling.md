---
link: []
aliases: [Database Concurrency]
date created: Jun 8th, 2023
date modified: Aug 12th, 2023
---

## Serializability
Serializability ensures that a schedule (i.e., the sequence of read/write operations) of multiple concurrent transactions is equivalent to some serial execution of those transactions.  
Major correctness criterion for concurrent transactions' executions and is considered the highest level of isolation between transactions

### Conflict Serializability 
If it can be transformed (swapped) into a serial schedule by swapping non-conflicting operations

### View Serializability
View equivalent to some serial schedule, meaning the outcome of the schedule is the same as if the transactions were executed one after another

## Two Phase Locking (2PL)

### Growing Phase (Locking)
The transaction may obtain locks, but cannot release any locks.  
transaction can obtain a shared (read) lock or exclusive (write) lock on a data item before it is read or written to.

### Shrinking Phase (Unlocking)
Once the transaction releases its first lock, the second phase starts, in which it can only release locks, but cannot obtain any new locks.  
The transaction keeps all the locks until it completes all 'write' operations to maintain isolation and consistency.

The purpose of two-phase locking is to ensure that all the conflicting operations are executed in an order that is equivalent to some serial order to avoid [[concurrency]] related issues like dirty reads, unrepeatable reads, and phantom reads.


## Links
- [[Lock]]
- [[Concurrency]]
- [[Database MVCC]]
- [[Database Isolation Level]]
- [[Database Errors]]
- [[Optimistic Concurrency Control]]