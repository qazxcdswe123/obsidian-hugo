## What
If the present bit is set to one, it means the page is present in physical memory and everything proceeds as above; if it is set to zero, the page is not in memory but rather on disk somewhere
The act of accessing a page that is not in physical memory.

A present bit (of some kind) must be included to tell us whether the page is present in memory or not.
When not, the operating system page fault handler runs to service the page fault, and thus arranges for the transfer of the desired page from disk to memory

A [[page]] fault is an interruption that occurs when a software program attempts to access a memory block not currently stored in the system's RAM. This [[exception]] tells the [[operating system]] to find the block in [[virtual memory]] so it can be sent from a device's storage to RAM.
The MMU detects the page fault, but the operating system's [kernel](https://en.wikipedia.org/wiki/Kernel_(operating_system) "Kernel (operating system)") handles the exception by making the required page accessible in the physical memory or denying an illegal memory access.

## Links
- [What is a Page Fault?](https://www.computerhope.com/jargon/p/pagefaul.htm)
- [[Page Table]]