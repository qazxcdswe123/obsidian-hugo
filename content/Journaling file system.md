---
aliases: []
date created: Jun 19th, 2023
date modified: Jun 19th, 2023
---

## Journaling file system
A journaling [[file system]] allows for quick file system recovery after a crash occurs by logging the metadata of files.  
By enabling file system logging, the system records every change in the metadata of the file into a reserved area of the file system. The actual write operations are performed after the logging of changes to the metadata has been completed.

1. Data write: Write data to final location; wait for completion (the wait is optional; see below for details).
2. Journal metadata write: Write the begin block and metadata to the log; wait for writes to complete.
3. Journal commit: Write the transaction commit block (containing TxE) to the log; wait for write to complete; transaction is said to be committed.
4. Checkpoint: Write the contents of the update (metadata and data) to their final on-disk locations.
5. Free: Some time later, mark the transaction free in the journal by updating the journal superblock.
- [[Write Ahead Log|WAL]]