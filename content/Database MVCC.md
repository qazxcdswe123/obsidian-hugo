## What
Multiversion Concurrency Control
Concurrency control method commonly used by database management systems to provide concurrent access to the database and in programming languages to implement transactional memory.

## How
Each SQL statement sees a snapshot of data (a _database version_) as it was some time ago, regardless of the current state of the underlying data. This prevents statements from viewing inconsistent data produced by concurrent transactions performing updates on the same data rows, providing _transaction isolation_ for each database session.

## Why
The main advantage of using the MVCC model of concurrency control rather than locking is that in MVCC locks acquired for querying (reading) data do not conflict with locks acquired for writing data, and so reading never blocks writing and writing never blocks reading.

## Links
- [PostgreSQL: Documentation: 15: Chapter 13. Concurrency Control](https://www.postgresql.org/docs/current/mvcc.html)