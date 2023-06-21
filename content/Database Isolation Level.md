## Database Isolation Level

| Isolation Level  | Dirty Read             | Nonrepeatable Read | Phantom Read           | Serialization Anomaly |
| ---------------- | ---------------------- | ------------------ | ---------------------- | --------------------- |
| Read uncommitted | Allowed, but not in PG | Possible           | Possible               | Possible              |
| Read committed   | Not possible           | Possible           | Possible               | Possible              |
| Repeatable read  | Not possible           | Not possible       | Allowed, but not in PG | Possible              |
| Serializable     | Not possible           | Not possible       | Not possible           | Not possible          |

### Read Uncommitted
A `SELECT` query (without a `FOR UPDATE/SHARE` clause) sees only data committed before the query began. It never sees either uncommitted data or changes committed during query execution by concurrent transactions.  
In effect, a `SELECT` query sees a snapshot of the database as of the instant the query begins to run.