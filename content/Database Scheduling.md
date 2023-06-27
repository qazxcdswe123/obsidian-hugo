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

## Locks
1.一级锁协议：事务T修改数据R之前，先加X锁，直到事务结束时释放（无论是正常结束commit还是非正常结束rollback）
作用：可防止 更新丢失问题。
不能防止： 脏读，不可重复读，幻读等。
PS：任何数据库都至少满足一级锁的协议，因为更新丢失是不能接受的错误，所以更新丢失一般只存在于理论讨论中，实际应用中基本不会出现这个问题。

2.二级锁协议：在一级锁的条件下，T在读取R之前先加S锁，读完后释放。
作用：可防止更新丢失，脏读。
不能防止： 不可重复读，幻读。

3.三级锁协议：在一级锁的条件下，T在读取R之前先加S锁，事务结束后释放。
作用：可防止 更新丢失，脏读，不可重复读，幻读。

## Links
- [[Locks]]
- [[Concurrency]]
- [[Database MVCC]]
- [[Database Isolation Level]]
- [[Database Errors]]