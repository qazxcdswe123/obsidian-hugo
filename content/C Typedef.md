---
aliases: []
tags: [] 
date created: Aug 12th, 2022
date modified: Sep 21st, 2022
---
## Typedef Normal

```c
typedef int myinteger;
typedef char *mystring;
typedef void (*myfunc)();

myinteger i;   // is equivalent to    int i;
mystring s;    // is the same as      char *s;
myfunc f;      // compile equally as  void (*f)();
```

One common situation is to use typedef names for various integer quantities, then make an appropriate set of choices of short, int, and long for each host machine.Types like `size_t` and `ptrdiff_t` from the standard library are examples.

The second purpose of typedefs is to provide better documentation for a program. A type called `Treeptr` may be easier to understand than one declared only as a pointer to a complicated structure.
## Typedef Function Pointer
URL: [c++ - Typedef function pointer? - Stack Overflow](https://stackoverflow.com/questions/4295432/typedef-function-pointer)
- **Why is typedef used?** To ease the reading of the code - especially for pointers to functions, or structure names.
- **The syntax looks odd (in the pointer to function declaration)** That syntax is not obvious to read, at least when beginning. Using a `typedef` declaration instead eases the reading
- **Is a function pointer created to store the memory address of a function?** Yes, a function pointer stores the address of a function. This has nothing to do with the `typedef` construct which only ease the writing/reading of a program ; the [[compiler]] just expands the typedef definition before compiling the actual code.

```cpp
typedef int (*t_somefunc)(int, int);

int product(int u, int v) {
  return u*v;
}

t_somefunc afunc = &product;
...
int x2 = (*afunc)(123, 456); // call product() to calculate 123*456
```