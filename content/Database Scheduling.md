---
aliases: [Database Concurrency]
date created: Jun 8th, 2023
date modified: Jun 11th, 2023
---

## Serializability
Serializability ensures that a schedule (i.e., the sequence of read/write operations) of multiple concurrent transactions is equivalent to some serial execution of those transactions.  
Major correctness criterion for concurrent transactions' executions and is considered the highest level of isolation between transactions

### Conflict Serializability 
A schedule is considered conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations

### View Serializability

## Types of Error

### dirty read
A transaction reads data written by a concurrent **uncommitted** transaction.  
Since it is uncommitted it may rollback, leading to a *dirty* read.

### nonrepeatable read
A transaction re-reads data it has previously read and finds that data has been modified by another transaction (that committed since the initial read).  
unmatched record.

### phantom read
A transaction **re-executes** a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction.

### serialization anomaly
The result of successfully committing a group of transactions is inconsistent with all possible orderings of running those transactions one at a time.

## Isolation Level

|Isolation Level|Dirty Read|Nonrepeatable Read|Phantom Read|Serialization Anomaly|
|------------------|------------------------|--------------------|------------------------|-----------------------|
| Read uncommitted | Allowed, but not in PG | Possible           | Possible               | Possible              |
| Read committed   | Not possible           | Possible           | Possible               | Possible              |
| Repeatable read  | Not possible           | Not possible       | Allowed, but not in PG | Possible              |
| Serializable     | Not possible           | Not possible       | Not possible           | Not possible          |

### Read Uncommitted
A `SELECT` query (without a `FOR UPDATE/SHARE` clause) sees only data committed before the query began. It never sees either uncommitted data or changes committed during query execution by concurrent transactions.  
In effect, a `SELECT` query sees a snapshot of the database as of the instant the query begins to run.

## Links
- [[Locks]]
- [[Concurrency]]
- [[Database MVCC]]