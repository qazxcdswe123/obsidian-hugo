---
aliases: []
tags: [] 
date created: Jul 18th, 2022
date modified: Jul 31st, 2022
---
## Special Register
- `%rsp` : [[Stack]] [[Pointer]] (Location of runtime [[stack]])
- `%rbp` : Frame [[Pointer]]
- `%rip` : [[CPU Instruction]] [[Pointer]] (Location of current code control point, or PC)
- `%rax` : Store return value

- callee saved register
	- `%rbx`
	- `%rbp`
	- `%r12-%r15`
> When procedure  P  calls procedure  Q ,  Q  must preserve the values of these registers, *ensuring that they have the same values when  Q  returns to  P  as they did when  Q  was called.* (P call Q, Q preserve)

> Procedure  Q can preserve a register value by either not changing it at all or by pushing the original value on the [[stack]], altering it, and then popping the old value from the [[stack]] before returning.

___
- caller saved register
	- All but `%rsp`
	- they can be modified by any function.
	- hold temporary quantities that need not be preserved across calls.-> caller's responsibility to save

___
- frame [[pointer]]
	- points to the base of the current [[stack]] frame

___
- argument [X86-64 Architecture Guide](http://6.s081.scripts.mit.edu/sp18/x86-64-architecture-guide.html)
	- `%rdi`  used to pass 1st argument
	- `%rsi`
	- `%rdx`
	- `%rcx`
	- `%r8`
	- `%r9`

- 32-bit
	- `%eax` through `%edx`
	- `%esi`, `%edi`, `%ebp`, `%esp`
	- `%r8d` through `%r15d`
- 64-bit
	- `%rax` through `%rdx`
	- `%rsi`, `%rdi`, `%rbp`, `%rsp`
	- `%r8` through `%r15`
	
![](https://img.ynchen.me/2022/07/51fbf373929ab0213c03db80b4b72a65.png)
