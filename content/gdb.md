---
aliases: []
date created: Aug 6th, 2022
date modified: Aug 6th, 2022
---
[[GDB Crash Course]]  
[[1. gdb 调试利器 — Linux Tools Quick Tutorial]]  

## Commands
- `disas` disassemble (default is current function)
- `where` / `frame` print the stack frame
- `si` step in instruction level

### Break
`b *0x400f30` set breakpoint at memory

### Format Letters
Examine memory: x/FMT ADDRESS.
Format letters are o(octal), x(hex), d(decimal), u(unsigned decimal),  t(binary), f(float), a(address), i(instruction), c(char), s(string)  

## Misc
`<C-x> + <C-a>`: Code view
