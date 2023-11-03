---
link: []
aliases: [Executable and Linkable Format]
date created: Jul 26th, 2023
date modified: Aug 28th, 2023
---
a common standard [file format](https://en.wikipedia.org/wiki/File_format "File format") for [executable](https://en.wikipedia.org/wiki/Executable "Executable") files, [object code](https://en.wikipedia.org/wiki/Object_code "Object code"), [shared libraries](https://en.wikipedia.org/wiki/Library_(computing) "Library (computing)"), and [core dumps](https://en.wikipedia.org/wiki/Core_dump "Core dump").

## Types
ELF files can have different types, such as:

- EXEC (Executable file)
- DYN (Shared object file), for libraries
- REL (Relocatable file), before being linked into an executable file
- CORE (Core dump file)

## Relocatable [[Object Files]]
| Sections    | Descriptions                                                                                                         |
| ----------- | -------------------------------------------------------------------------------------------------------------------- |
| `.text`     | machine code of the compiled program                                                                                 |
| `.rodata`   | format strings or jump tables for `switch` ...                                                                       |
| `.data`     | *Initialized* global and static C variables                                                                          |
| `.bss`      | *Uninitialized* global and static C variables, plus global or static variables initialized to 0, Do not occupy space |
| `.symtab`   | *symbol table* about functions and global variables that are defined and referenced in the program                   |
| `.rel.text` | contains relocation information for the `.text` section                                                              |
| `.rel.data` | relocation information for the `.data` section                                                                       |
| `.debug`    | debugging symbol table                                                                                               |
| `.line`     | mapping between line numbers in the C and machine code instructions in `.text`                                       |
| `.strtab`   | string table for symbol tables in `.symtab` and `.debug`                                                                                                                     |


## Links
- [Executable and Linkable Format - Wikipedia](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)
- [[ABI]]
- [[Linker]]