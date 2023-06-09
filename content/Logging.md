---
aliases: []
date created: Jun 7th, 2023
date modified: Jun 8th, 2023
---

## Logging
![image.png](https://img.ynchen.me/2023/04/8829efe9215f8d4a840662f75b68f57a.webp)

## DBMS
In [[DBMS]], log files typically contain:
1. **Transaction ID**: This uniquely identifies the transaction that made the change.
2. **Operation Type**: This denotes the type of operation that was performed, such as INSERT, UPDATE, DELETE, or SELECT.
3. **Data**: The data that was changed by the operation. This might include both the old value (before the change) and the new value (after the change).
4. **Timestamp**: The time at which the operation was performed.
5. **Status**: The status of the transaction, such as "start", "commit", or "abort".
6. **Table Name or Record ID**: An identifier for the table or record that was changed.

## Links
- [[Write Ahead Log]]