---
aliases: []
tags: []
date created: Nov 24th, 2022
date modified: Mar 29th, 2023
---

# File Permission
[File-system permissions - Wikipedia](https://en.wikipedia.org/wiki/File-system_permissions)  
Two types of permissions are widely available: traditional Unix file system permissions and **[access-control lists](https://en.wikipedia.org/wiki/Access-control_list "Access-control list") (ACLs)** which are capable of more specific control.

## `chown`
Change the owner of file.  
`user:group`

## `chmod`
Change file permission  
`chmod permissions filename`  
There are 2 ways to use the command –
1. **Absolute mode**
2. **Symbolic mode**

Use mask to get the result. Maximum is `111`, the left-most bit is `read`, middle bit is `write`, right-most bit is `execute`.

## Sudo
```shell
# Adding User to the sudo Group
usermod -aG sudo username
```

## Traditional Unix Permissions
- The read bit adds 4 to its total (in binary 100),
- The write bit adds 2 to its total (in binary 010), and
- The execute bit adds 1 to its total (in binary 001).

## Links
- [[Linux User]]  
- [chown(1): change file owner/group - Linux man page](https://linux.die.net/man/1/chown)
