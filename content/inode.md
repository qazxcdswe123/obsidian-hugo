---
aliases: []
date created: Aug 29th, 2022
date modified: Jun 19th, 2023
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

## `stat`
**To see the metadata for a certain file**, we can use the `stat()` or `fstat()` system calls. These calls take a pathname (or file descriptor) to a file and fill in a stat structure.

```c
struct stat {
  dev_t st_dev; // ID of device containing file
  ino_t st_ino; // inode number
  mode_t st_mode; // protection
  nlink_t st_nlink; // number of hard links
  uid_t st_uid; // user ID of owner
  gid_t st_gid; // group ID of owner
  dev_t st_rdev; // device ID (if special file)
  off_t st_size; // total size, in bytes
  blksize_t st_blksize; // blocksize for filesystem I/O
  blkcnt_t st_blocks; // number of blocks allocated
  time_t st_atime; // time of last access
  time_t st_mtime; // time of last modification
  time_t st_ctime; // time of last status change
};
```

## Links
- [[File System]]
- [[Linux Storage]]