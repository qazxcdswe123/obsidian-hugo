---
aliases: [WAL]
date created: Jun 8th, 2023
date modified: Jun 8th, 2023
---

## How
- Append only file for changes that will be made to the database.
- Before applying changes, write to WAL first
- Implement record structure

```
record:
	length: uint32      // length of data section
	checksum: uint32    // CRC32 checksum of data
	data: byte[length]  // serialized ddb.internal.LogRecord proto
```

- Periodically perform checkpoints ([[Database Failure]]), which involve writing all the changes specified in the WAL to the database and clearing the log.