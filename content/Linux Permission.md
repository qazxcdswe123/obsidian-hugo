---
aliases: []
date created: Nov 24th, 2022
date modified: Jun 19th, 2023
---

## File Permission
The permissions consist of three groupings: what the **owner** of the file can do to it, what someone in a **group** can do to the file, and finally, what anyone (sometimes referred to as **other**) can do.

### `chown`
Change the owner of file.  
`user:group`

### `chmod`
Change file permission  
`chmod permissions filename`  
There are 2 ways to use the command –
1. **Absolute mode**
2. **Symbolic mode**

Use mask to get the result. Maximum is `111`, the left-most bit is `read`, middle bit is `write`, right-most bit is `execute`.

- The read bit adds 4 to its total (in binary 100),
- The write bit adds 2 to its total (in binary 010), and
- The execute bit adds 1 to its total (in binary 001).

### Sudo Group
```shell
# Adding User to the sudo Group
usermod -aG sudo username
```

### Links
- [[Linux User]]  
- [chown(1): change file owner/group - Linux man page](https://linux.die.net/man/1/chown)
- [[Protection Ring]]
