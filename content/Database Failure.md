## Recovery
### Checkpointing
Save the current state of the database to disk, allowing for faster recovery in case of a system failure or crash.
It ensures that all committed transactions and changes made to the database are saved, and it also includes a log of all transactions that have occurred since the last checkpoint.

- [[Write Ahead Log]]