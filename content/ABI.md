---
aliases: [Application Binary Interface]
date created: Feb 13th, 2023
date modified: Jul 26th, 2023
---
It defines how data structures or computational routines are accessed in machine code, which is a low-level, [[hardware]]-dependent format

ABIs cover various details, such as data type, size, and alignment; calling conventions, which control how functions' arguments are passed and return values retrieved; and [[syscall|system call]] numbers and how an application should make system calls to the [[operating system]]

- Your API defines the order in which you pass arguments to a function. 
- While your ABI defines the mechanics of _how_ these arguments are passed (registers, [[stack]], etc.).

## Links
- [compiler construction - What is an application binary interface (ABI)? - Stack Overflow](https://stackoverflow.com/questions/2171177/what-is-an-application-binary-interface-abi)