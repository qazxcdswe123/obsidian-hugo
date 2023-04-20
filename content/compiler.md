---
aliases: []
date created: Aug 15th, 2022
date modified: Apr 10th, 2023
---
- Preprocessing phase [C preprocessor - Wikipedia](https://en.wikipedia.org/wiki/C_preprocessor)
	- A preprocessing step performs macro substitution on program text, inclusion of other source files, and conditional compilation.
- Compilation phase
- Assembly phase
- Linking phase
- [Understanding the differences: traditional interpreter, JIT compiler, JIT interpreter and AOT compiler - Software Engineering Stack Exchange](https://softwareengineering.stackexchange.com/questions/246094/understanding-the-differences-traditional-interpreter-jit-compiler-jit-interp)

1. _Source Code_ → **Lexical Analysis** → _Tokens_
2. _Tokens_ → **Syntactic Analysis** → _Abstract Syntax Tree_
3. _Abstract Syntax Tree_ → **Various Transformations** → _Some Intermediate Representation_
4. _Some Intermediate Representation_ → **Code Generation** → {_Machine,Byte,Source} Code_

## [[Optimization]]

## Links
- [Executable and Linkable Format - Wikipedia](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)
- [compiler construction - How does compiling circular dependencies work? - Stack Overflow](https://stackoverflow.com/questions/3032874/how-does-compiling-circular-dependencies-work)
	- Two pass or multi pass compiler to deal with circular dependencies
- [GitHub - jamiebuilds/the-super-tiny-compiler: Possibly the smallest compiler ever](https://github.com/jamiebuilds/the-super-tiny-compiler) [[todo]]
___
- [[JIT Compiler]]
- [[Interpreter]]