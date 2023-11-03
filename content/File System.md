---
aliases: []
date created: Jan 1st, 2023
date modified: Jun 19th, 2023
---

## Mental Model
A file system relies on data structures _about_ the files, as opposed to the contents of that file. The former are called _[metadata](https://en.wikipedia.org/wiki/Metadata "Metadata")_—data that describes data. Each file is associated with an _[[inode]]_, which is identified by an integer, often referred to as an _i-number_ or _[[inode]] number_.

- What on-disk structures store the file system’s data and metadata? 
- What happens when a [[process]] opens a file? 
- Which on-disk structures are accessed during a read or write?

## How

### [[Bitmap]]
When mounting a file system, the [[operating system]] will read the superblock first, to initialize various parameters, and then attach the volume to the file-system tree. When files within the volume are accessed, the system will thus know exactly where to look for the needed on-disk structures.

### Directory
Often, file systems treat directories as a special type of file. Thus, a directory has an inode, somewhere in the inode table (with the type field of the inode marked as “directory” instead of “regular file”). The directory has data blocks pointed to by the inode (and perhaps, indirect blocks); these data blocks live in the data block region of our simple file system. Our on-disk structure thus remains unchanged.

### [[Cache]]
Some applications (such as databases) don’t enjoy this trade-off. Thus, to avoid unexpected data loss due to write buffering, they simply force writes to disk, by calling **`fsync()`**, by using **direct [[IO|I/O]] interfaces** that work around the cache, or by using the **raw disk interface** and avoiding the file system altogether.

## Links
- [[Ext4]]
- [[Journaling file system]]