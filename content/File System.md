---
aliases: [FS]
tags: []
date created: Jan 1st, 2023
date modified: Jan 2nd, 2023
---
## File System
A file system relies on data structures _about_ the files, as opposed to the contents of that file. The former are called _[metadata](https://en.wikipedia.org/wiki/Metadata "Metadata")_—data that describes data. Each file is associated with an _[[inode]]_, which is identified by an integer, often referred to as an _i-number_ or _[[inode]] number_.

### Journaling file system
A journaling file system allows for quick file system recovery after a crash occurs by logging the metadata of files.  
By enabling file system logging, the system records every change in the metadata of the file into a reserved area of the file system. The actual write operations are performed after the logging of changes to the metadata has been completed.

## Links
- [[inode]]