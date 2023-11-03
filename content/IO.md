---
aliases: [I/O]
date created: Jul 10th, 2022
date modified: Jun 19th, 2023
---

## How
It may be best to use a hybrid that polls for a little while and then, if the device is not yet finished, uses interrupts. This two-phased approach may achieve the best of both worlds.

## IO Measuring
- iostat, sar, node exporter or anything else that takes figures from /proc come from level 5.
- bcc ([[eBPF]]) tools biosnoop, biolatency, biotop comes from level 5.
- bcc ([[eBPF]]) tools xfsdist and xfsslower come from from level 3.
- perf trace, strace come from level 3.
- application figures come from level 1.

## File IO
A file is a sequence of bytes, nothing more and nothing less. Every I/O device, including disks, keyboards, displays, and even networks, is modeled as a file.  
- [[C++ File]]  
- [[Python File]]

### `fsync()`
When a [[process]] calls `fsync()` for a particular file descriptor, the [[file system]] responds by forcing all dirty (i.e., not yet written) data to disk, for the file referred to by the specified file descriptor. The `fsync()` routine returns once all of these writes are complete.

## STDIOE
- [[Shell]]  
- `2>&1`  
File descriptor 1 is the standard output (`stdout`).  
File descriptor 2 is the standard error (`stderr`).

At first, `2>1` may look like a good way to redirect `stderr` to `stdout`. However, it will actually be interpreted as "redirect `stderr` to a file named `1`".  
`&` indicates that what follows and precedes is a _file descriptor_, and not a filename. Thus, we use `2>&1`. Consider `>&` to be a redirect merger operator.
`&` is only interpreted to mean "file descriptor" in the context of redirections. Writing `command &2>&` is parsed as `command &` and `2>&1`, i.e. "run `command` in the background, then run the command `2` and redirect its stdout into its stdout".

## Links
- [[Operating System|OS]]