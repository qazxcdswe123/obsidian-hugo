---
aliases: []
date created: Jul 29th, 2022
date modified: Jul 29th, 2022
---
- [[Instruction Level Parallelism]]

## Data Manipulation
- `mov`
	- From [[memory]] to [[register]], vice versa; Immediate to register or memory, register to register.
	- Move to register in 64bits, need `movq`
- `add`
- `lea`
	- `leaq S, D` : Move `&S` to `D`
![](https://img.ynchen.me/2022/07/86193bce90b8a58026911491ce0d7b76.png)

## Control
### Movement
See also [[Condition Code]]
- `cmp`
	- `cmpq S1, S2`
	- Based on `S2 - S1`, so `jg` means `S2 > S1`
- `test`
	- The test instructions behave in the same manner as the and instructions, except that they set the condition codes without altering their destinations.
- `set`
	- Used to access condition code
- `jmp`
	- It can be either a direct jump, where the jump target is encoded as part of the instruction, or an indirect jump, where the jump target is read from a register or a memory location.
		- `jmp *%rax` : direct
		- `jmp *(%rax)` : indirect
	- Use PC relative???? [Addressing mode - Wikipedia](https://en.wikipedia.org/wiki/Addressing_mode)
		- they encode the difference between the address of the target instruction and the address of the instruction immediately following the jump.
![](https://img.ynchen.me/2022/08/0159aef39b16bc65247d47273730d15d.png)


### Conditional Branches
- [[Condition Code]]
