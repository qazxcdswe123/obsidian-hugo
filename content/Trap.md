> A **trap** is an [[exception]] that is reported immediately following the execution of the trapping instruction. Traps allow execution of a program or task to be continued without loss of program continuity. The return address for the trap handler points to the instruction to be executed after the trapping instruction.

The hardware needs to be a bit careful when executing a trap, in that it must make sure to save enough of the caller’s registers in order to be able to return correctly when the OS issues the return-from-trap instruction.
On x86, for example, the processor will push the **program counter, flags, and a few other registers onto a per-process kernel stack**; the return-fromtrap will pop these values off the stack and resume execution of the usermode program (see the Intel systems manuals for details). Other hardware systems use different conventions, but the basic concepts are similar across platforms.

## Where to jump?
The kernel does so by setting up a trap table at boot time. When the machine boots up, it does so in privileged (kernel) mode, and thus is free to configure machine hardware as need be. One of the first things the OS thus does is to tell the hardware what code to run when certain exceptional events occur.

## Links
- [[Linux]]
- [[syscall]]