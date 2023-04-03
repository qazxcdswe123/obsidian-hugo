> **Interrupts** occur at random times during the execution of a program, in response to signals from hardware. System hardware uses interrupts to handle events external to the processor, such as requests to service peripheral devices. Software can also generate interrupts by executing the INT n instruction.

**1. Maskable Interrupt :**  
An Interrupt that can be disabled or ignored by the instructions of CPU are called as Maskable Interrupt.The interrupts are either edge-triggered or level-triggered or level-triggered.

**2. Non-Maskable Interrupt :**  
An interrupt that cannot be disabled or ignored by the instructions of CPU are called as Non-Maskable Interrupt.A Non-maskable interrupt is often used when response time is critical or when an interrupt should never be disable during normal system operation. Such uses include reporting non-recoverable hardware errors, system debugging and profiling and handling of species cases like system resets.

## Links
- [Difference between Maskable and Non Maskable Interrupt - GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-maskable-and-non-maskable-interrupt/?utm_source=pocket_saves)
- [[Page Fault]]