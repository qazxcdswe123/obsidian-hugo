---
aliases: [FS]
date created: Jan 1st, 2023
date modified: Jan 2nd, 2023
---
## File System
A file system relies on data structures _about_ the files, as opposed to the contents of that file. The former are called _[metadata](https://en.wikipedia.org/wiki/Metadata "Metadata")_—data that describes data. Each file is associated with an _[[inode]]_, which is identified by an integer, often referred to as an _i-number_ or _[[inode]] number_.

### Journaling file system
A journaling file system allows for quick file system recovery after a crash occurs by logging the metadata of files.  
By enabling file system logging, the system records every change in the metadata of the file into a reserved area of the file system. The actual write operations are performed after the logging of changes to the metadata has been completed.

# Ext4

## `HTree`
- [HTree - Wikipedia](https://en.wikipedia.org/wiki/HTree)
Use [[B-Tree]] for directory indexing.
It is constant depth of either one or two levels, have a high fanout factor, use a [hash](https://en.wikipedia.org/wiki/Hash_table "Hash table") of the [filename](https://en.wikipedia.org/wiki/Filename "Filename"), and do not require [balancing](https://en.wikipedia.org/wiki/Balanced_tree "Balanced tree").

## Links
- [[inode]]
