---
aliases: []
link: []
date created: Aug 1st, 2023
date modified: Aug 10th, 2023
---

## Checkpointing
Save the current state of the database to disk, allowing for faster recovery in case of a system failure or crash.  
It ensures that all committed transactions and changes made to the database are saved, and it also includes a log of all transactions that have occurred since the last checkpoint.

- [[Write Ahead Log]]
- [[Checksum]]