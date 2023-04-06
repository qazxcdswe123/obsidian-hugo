---
aliases: []
date created: Jul 10th, 2022
date modified: Apr 4th, 2023
---

## IO Performance

### Measuring
- iostat, sar, node exporter or anything else that takes figures from /proc come from level 5.
- bcc ([[ebpf]]) tools biosnoop, biolatency, biotop comes from level 5.
- bcc ([[ebpf]]) tools xfsdist and xfsslower come from from level 3.
- perf trace, strace come from level 3.
- application figures come from level 1.

## File IO
A file is a sequence of bytes, nothing more and nothing less. Every I/O device, including disks, keyboards, displays, and even networks, is modeled as a file.  
- [[C++ File]]  
- [[Python File]]

## STDIOE
- [[Shell]]  
- [bash - In the shell, what does " 2>&1 " mean? - Stack Overflow](https://stackoverflow.com/questions/818255/in-the-shell-what-does-21-mean)

- `2>&1`  
File descriptor 1 is the standard output (`stdout`).  
File descriptor 2 is the standard error (`stderr`).

At first, `2>1` may look like a good way to redirect `stderr` to `stdout`. However, it will actually be interpreted as "redirect `stderr` to a file named `1`".  
`&` indicates that what follows and precedes is a _file descriptor_, and not a filename. Thus, we use `2>&1`. Consider `>&` to be a redirect merger operator.

`&` is only interpreted to mean "file descriptor" in the context of redirections. Writing `command &2>&` is parsed as `command &` and `2>&1`, i.e. "run `command` in the background, then run the command `2` and redirect its stdout into its stdout".

## Links
- [[Operating System|OS]]
