---
aliases: [Executable and Linkable Format]
date created: Jul 26th, 2023
date modified: Jul 26th, 2023
---
a common standard [file format](https://en.wikipedia.org/wiki/File_format "File format") for [executable](https://en.wikipedia.org/wiki/Executable "Executable") files, [object code](https://en.wikipedia.org/wiki/Object_code "Object code"), [shared libraries](https://en.wikipedia.org/wiki/Library_(computing) "Library (computing)"), and [core dumps](https://en.wikipedia.org/wiki/Core_dump "Core dump").

## Layout
Each ELF file is made up of one ELF header, followed by file data. The data can include:

- Program header table, describing zero or more [memory segments](https://en.wikipedia.org/wiki/Memory_segmentation "Memory segmentation")
- Section header table, describing zero or more sections
- Data referred to by entries in the program header table or section header table

## Types
ELF files can have different types, such as:

- EXEC (Executable file)
- DYN (Shared object file), for libraries
- REL (Relocatable file), before being linked into an executable file
- CORE (Core dump file)

## Links
- [Executable and Linkable Format - Wikipedia](https://en.wikipedia.org/wiki/Executable_and_Linkable_Format)
- [[ABI]]