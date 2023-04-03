---
aliases: []
date created: Nov 27th, 2022
date modified: Feb 26th, 2023
---

## Exception Safe
- [How to: Design for exception safety | Microsoft Learn](https://learn.microsoft.com/en-us/cpp/cpp/how-to-design-for-exception-safety?view=msvc-170)  
The general rule is that you should not release your resources until you have the replacement ready.

## Exceptions in CPU
> **Exceptions** occur when the processor detects an error condition while executing an instruction, such as division by zero. The processor detects a variety of error conditions including protection violations, page faults, and internal machine faults.

> **Exceptions** are classified as **faults**, **[[trap|traps]]**, or **aborts** depending on the way they are reported and whether the instruction that caused the exception can be restarted without loss of program or task continuity.

