---
aliases: []
tags: []
date created: Aug 29th, 2022
date modified: Aug 29th, 2022
---
[What are inodes in Linux? -](https://docs.rackspace.com/support/how-to/what-are-inodes-in-linux/)  
Linux must allocate an index node (inode) for every file and directory in the filesystem. Inodes do not store actual data. Instead, they store the metadata where you can find the storage blocks of each file’s data.

#### Metadata in an Inode
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