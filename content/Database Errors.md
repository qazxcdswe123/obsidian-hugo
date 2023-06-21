---
aliases: []
date created: Jun 21st, 2023
date modified: Jun 21st, 2023
---

## dirty read
A transaction reads data written by a concurrent **uncommitted** transaction.  
Since it is uncommitted it may **rollback** (and leave to a wrong data being read), leading to a *dirty* read.

## nonrepeatable read
A transaction **re-reads** data it has previously read and finds that data has been **modified** by another transaction (that committed since the initial read).  
Leading to a unmatched record.

## phantom read
A transaction **re-executes** a query returning a set of rows that satisfy a search condition and finds that the set of rows satisfying the condition has changed due to another recently-committed transaction.

## serialization anomaly
The result of successfully committing a group of transactions is inconsistent with all possible orderings of running those transactions one at a time.