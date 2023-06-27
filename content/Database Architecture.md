---
aliases: []
date created: Jun 26th, 2023
date modified: Jun 26th, 2023
---
1. **Physical Level (Internal Level):** This is the lowest level of the three-tier architecture. It describes how the data is physically stored in the system, including details about storage devices, indexes, data access paths, and more. It is concerned with managing the actual storage, retrieval, and update of data in a database. This level is usually handled by database administrators and isn't exposed to end-users.
2. **Logical Level (Conceptual Level):** This is the intermediate level that defines what data is stored in the database and the relationships among the data. It hides the complexities of the physical level and provides an abstract view of the data to the users. It involves things like tables, views, indexes, etc.
3. **View Level (External Level):** This is the highest level of the architecture and it describes how the data is seen by individual users. Different users might have different views of the system; for example, a salesperson will see a different aspect of the database than an operations manager. It's a way of organizing and presenting database information in a way that makes sense to different user groups.