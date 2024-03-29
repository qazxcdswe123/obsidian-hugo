## Static Linking
**1. Symbol Resolution:** Object files **define and reference** symbols, where each symbol corresponds to a **function, a global variable, or a static variable** (i.e., any C variable declared with the static attribute). The purpose of symbol resolution is to associate each symbol reference with exactly one symbol definition.

**2. Relocation:** Compilers and assemblers generate code and data sections that start at address 0. The linker **relocates** these sections by associating a memory location with each symbol definition, and then modifying all of the references to those symbols so that they point to this memory location. The linker blindly performs these relocations using detailed instructions, generated by the assembler, called **relocation entries**.

## Symbols
- Global symbols
	- defined by module `m` and can be referenced by others
	- referenced by module `m` and defined by others
- Local symbols

## Links
- [Linker (computing) - Wikipedia](https://en.wikipedia.org/wiki/Linker_(computing))
- [[Object Files]]