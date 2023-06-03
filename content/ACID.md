---
aliases: []
date created: May 21st, 2023
date modified: May 21st, 2023
---
- Atomicity: Each statement in a transaction (to read, write, update or delete data) is treated as a single unit. Either the entire statement is executed, or none of it is executed. This property prevents data loss and corruption from occurring if, for example, if your streaming data source fails mid-stream.
- Consistency: Transactions only make changes to tables in predefined, predictable ways. Transactional consistency ensures that corruption or errors in your data do not create unintended consequences for the integrity of your table.
- Isolation: When multiple users are reading and writing from the same table all at once, isolation of their transactions ensures that the concurrent transactions don't interfere with or affect one another. Each request can occur as though they were occurring one by one, even though they're actually occurring simultaneously.
- Durability: Ensures that changes to your data made by successfully executed transactions will be saved, even in the event of system failure.
	- [[Write Ahead Log]]