---
aliases: []
tags: []
date created: Aug 6th, 2022
date modified: Aug 6th, 2022
---
[[gdb 简明使用教程]]  
[[1. gdb 调试利器 — Linux Tools Quick Tutorial]]  
[[CS107 GDB and Debugging]]

## Commands
- `disas` disassemble (default is current function)
- `where` / `frame` print the stack frame
- `si` step in instruction level

### Break
`b *0x400f30` set breakpoint at memory

### Format Letters
Examine memory: x/FMT ADDRESS.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),  t(binary), f(float), a(address), i(instruction), c(char), s(string)  


