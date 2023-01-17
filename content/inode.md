---
aliases: []
tags: []
date created: Aug 29th, 2022
date modified: Jan 2nd, 2023
---
- [What are inodes in Linux? -](https://docs.rackspace.com/support/how-to/what-are-inodes-in-linux/)  
Linux must allocate an index node (inode) for every file and directory in the filesystem. Inodes do not store actual data. Instead, they store **the metadata where you can find the storage blocks of each file’s data.**

In other words, a "file" is actually composed of three different things:

1. a PATH in the filesystem
2. an inode with metadata
3. data blocks pointed to by the inode

## Metadata in an Inode
The following metadata exists in an inode:
- File type
- Permissions
- Owner ID
- Group ID
- Size of file
- Time last accessed
- Time last modified
- Soft/Hard Links
- Access Control List (ACLs)

## Check the Inode Number in a Specific File
The command `stat` displays the file statistics, including the unique inode number:

[[File System]]