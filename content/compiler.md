---
link: []
aliases:
  - Compilers
date created: Aug 15th, 2022
date modified: Oct 26th, 2023
---

## Stages
- Lexical Analysis
- Parsing
- Semantic Analysis
- [[Optimization]]
- Code Generation

## Abstraction
- Abstraction = detached from concrete details 
	- “Abstraction is selective ignorance” - Andrew Koenig
- Modes of abstraction
	- Via languages/compilers: High-level code, few machine dependencies Via functions and subroutines: Abstract interface to behavior
	- Via modules: Export interfaces; hide implementation
	- Via classes/abstract data types: Bundle data with its operations

## Challenges
- **Error handling** (“When I encounter code which is incomplete or erroneous, I would like to present the user with a helpful message for each error in the program instead of immediately dying with an unhelpful message at the first error.”)
- **Syntax challenges** (“When you encounter a `-`, is it unary negation or a minus sign?”)
- **Semantics challenges** (“Can I correctly resolve function overloads per the PL specification for each invocation?”)
- **Typing challenges** (“Does the compiler determine type correctness via type inference, type checking, or ‘both’?”)

## Links
- [Understanding the differences: traditional interpreter, JIT compiler, JIT interpreter and AOT compiler - Software Engineering Stack Exchange](https://softwareengineering.stackexchange.com/questions/246094/understanding-the-differences-traditional-interpreter-jit-compiler-jit-interp)
- [compiler construction - How does compiling circular dependencies work? - Stack Overflow](https://stackoverflow.com/questions/3032874/how-does-compiling-circular-dependencies-work)
	- Use two pass or multi pass compiler to deal with circular dependencies
- [GitHub - jamiebuilds/the-super-tiny-compiler: Possibly the smallest compiler ever](https://github.com/jamiebuilds/the-super-tiny-compiler)
- [[JIT Compiler]]
- [[Interpreter]]
- [[Compilation]]
- [[ELF]]
- [[Finite Automata]]
- [[gcc]]

## Resources
- [Software Foundations](https://softwarefoundations.cis.upenn.edu/)
- [scheme2006.cs.uchicago.edu/11-ghuloum.pdf](http://scheme2006.cs.uchicago.edu/11-ghuloum.pdf)