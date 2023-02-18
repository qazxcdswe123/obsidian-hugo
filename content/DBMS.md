---
aliases: []
tags: []
date created: Feb 18th, 2023
date modified: Feb 18th, 2023
---

# DBMS
- Parsing & Optimization
- Relational Operators
	- Purpose: Execute a dataflow by operating on records and files
- Files and Index Management
	- Purpose: Organize tables and Records as groups of pages in a logical file
- Buffer Management
	- Provide the illusion of operating in memory
- Disk Space Management
	- Translate page requests into physical bytes on one or more device(s)

## DB File Structures
- Unordered Heap Files
	- Records placed arbitrarily across pages
	- [[Linked list]] or [[Page directory]]
- Clustered Heap Files
	- Records and pages are grouped
- Sorted Files
	- Pages and records are in sorted order
- Index Files
	- B+ Trees, Linear Hashing, …
	- May contain records or point to records in other files

## Records
### Fixed Length Records (FLR)
- Unpacked
	- [[Bitmap]]

### Variable Length Records (VLR)
