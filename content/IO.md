---
aliases: []
tags: []
date created: Jul 10th, 2022
date modified: Nov 17th, 2022
---
#Programming/Misc 

## Files
A file is a sequence of bytes, nothing more and nothing less. Every I/O device, including disks, keyboards, displays, and even networks, is modeled as a file.  
[[C++ File]]  
[[Python File]]

## Stream
Every stream in [[C++]] is tied to an output stream, which can be `null`.

What does this mean? First of all, it's important to understand that when you write `std::cout << "asdf"`, it is not necessarily immediately printed on the screen. It turns out that it is much better (in terms of performance) to collect it into a _buffer_ and then, at some point, _flush_ the buffer — i.e. empty its contents to the screen (or file, or any other "device"), all at once.

> By default, the standard narrow streams `cin` and `cerr` are tied to `cout`

In general I think people should read the documentation for such things instead of just pasting them "because it makes input faster".

## STDIOE
[[Shell]]  
[bash - In the shell, what does " 2>&1 " mean? - Stack Overflow](https://stackoverflow.com/questions/818255/in-the-shell-what-does-21-mean)

- `2>&1`  
File descriptor 1 is the standard output (`stdout`).  
File descriptor 2 is the standard error (`stderr`).

At first, `2>1` may look like a good way to redirect `stderr` to `stdout`. However, it will actually be interpreted as "redirect `stderr` to a file named `1`".  
`&` indicates that what follows and precedes is a _file descriptor_, and not a filename. Thus, we use `2>&1`. Consider `>&` to be a redirect merger operator.

`&` is only interpreted to mean "file descriptor" in the context of redirections. Writing `command &2>&` is parsed as `command &` and `2>&1`, i.e. "run `command` in the background, then run the command `2` and redirect its stdout into its stdout".

## Links
- [[Operating System|OS]]