---
aliases: 
tags: [CSAPP, Programming/Misc]
date: Jul 25th, 2022
---
- [[Stack Data Structure]]

[architecture - Why do stacks typically grow downwards? - Stack Overflow](https://stackoverflow.com/questions/2035568/why-do-stacks-typically-grow-downwards)
## Stack Pointer
The Stack Pointer (SP) register is used to indicate the location of the last item put item put onto the stack.
When you PUT something ONTO the stack (PUSH onto the stack), the SP is decremented before the item is e item is placed on the stack. 
When you take something OFF of the stack (PULL from the stack), the SP is incremented after the item is e item is pulled from the stack.
Before you can use a stack you have to initialize the SP to point to one value higher than the highest memory location in the stack.

### The stack is an array of memory dedicated to temporary storage
- SP points to location last item placed in block 
- SP **decreases** when you put an item on the stack 
- SP **increases** when you pull the item from the stack

## Stack Frame
> A stack frame is a memory management technique used in some programming languages for generating and eliminating temporary variables. In other words, it can be considered the collection of all information on the stack pertaining to a subprogram call. Stack frames are only existent during the runtime process. Stack frames help programming languages in supporting recursive functionality for subroutines.

A stack frame is comprised of:
- Local variables
- Saved copies of registers modified by subprograms that could need restoration
- Argument parameters
- Return address