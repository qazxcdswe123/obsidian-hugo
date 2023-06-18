---
aliases: []
date created: Jun 17th, 2023
date modified: Jun 17th, 2023
---
Memory Management Methods
- Used in [[Operating System|OS]]

## Free List
- [Free list - Wikipedia](https://en.wikipedia.org/wiki/Free_list)  
Use [[linked list]], when we need to allocate memory we simply move the head to next and use the head, when we free the memory we insert it back to head.

## `free`
Use an extra information in a **header** block which is kept in memory, usually just before the handed-out chunk of memory.

```c
typedef struct { int size; int magic; } header_t;

void free(void *ptr) {
	header_t *hptr = (header_t *) ptr - 1;
	...
}
```