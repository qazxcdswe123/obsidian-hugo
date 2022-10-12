---
aliases: []
tags: []
date created: Oct 11th, 2022
date modified: Oct 12th, 2022
---
Greatly inspired(copied) by: [Learn C in Y Minutes](https://learnxinyminutes.com/docs/c/) and [Learn C++ in Y Minutes](https://learnxinyminutes.com/docs/c++/)

## Introduction
- What will be covered in this tutorial?
	- Things that every [[Programming Language]] have in common!
	- Things that newbie programmers should know
		- Functions
		- Code style
		- Basic design
	- Memory([[Pointer]], Struct etc.)
	- Your questions
- What will **not be** covered?
	- Grammar
		- It is what it is!
	- Everything that I consider 谭浩强 related
		- Don't learn from it, get a new book instead! See [The Definitive C Book Guide and List - Stack Overflow](https://stackoverflow.com/questions/562303/the-definitive-c-book-guide-and-list) and [c++ faq - The Definitive C++ Book Guide and List - Stack Overflow](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)
		- i++++i
		- etc. (Just too many...)
	- **Details** (Will be partially covered in this text)
	- Compilation

## How a Program is Constructed
- By multiple files
- In files, we have multiple functions
- In functions, we have multiple data

Let's start with primitive data type in C

### Primitive Data Types in C
[Data Types in C - GeeksforGeeks](https://www.geeksforgeeks.org/data-types-in-c/)

| Type    | Size (in 64bit machine) | Comment                       |
| ------- | ----------------------- | ----------------------------- |
| short   | 2bytes                  | Integer                       |
| int     | 4bytes                  | Integer                       |
| long    | 8bytes                  | Integer                       |
| float   | 4bytes                  | Floating point number         |
| double  | 8bytes                  | Floating point number         |
| char    | 1byte                   | ASCII Char                    |
| pointer | 8bytes                  | Pointers are 8 bytes in 64bit |

Use the `sizeof` operator to check the size!

```c
// ints are usually 4 bytes (use the `sizeof` operator to check)
int x_int = 0;

// shorts are usually 2 bytes (use the `sizeof` operator to check)
short x_short = 0;

// chars are defined as the smallest addressable unit for a processor. 
// This is usually 1 byte
char y_char = 'y'; // Char literals are quoted with ''

// In C++, character literals are chars
sizeof('c') == sizeof(char) == 1

// In C, character literals are ints
sizeof('c') == sizeof(int)

// longs are often 8 bytes; long longs are guaranteed to be at least 8 bytes
long x_long = 0;
long long x_long_long = 0;

// floats are usually 32-bit floating point numbers
float x_float = 0.0f; // 'f' suffix here denotes floating point literal

// doubles are usually 64-bit floating-point numbers
double x_double = 0.0; // real numbers without any suffix are doubles

// integer and char types may be unsigned (greater than or equal to zero)
unsigned short ux_short;
unsigned int ux_int;
unsigned long long ux_long_long;
unsigned char uc;
```

You use this syntax to defined variables, so you can use it to build bigger program later on.

```c
// \t for tab
// \n for new line
#include <stdio.h>

int main(){
    printf("size of char is:\t\t%ld byte\n",sizeof(char));
    printf("size of int is:\t\t\t%ld bytes\n",sizeof(int));
    printf("size of unsigned int is:\t%ld bytes\n",sizeof(unsigned int));
    printf("size of long is:\t\t%ld bytes\n",sizeof(long));
    printf("size of unsigned long is:\t%ld bytes\n",sizeof(unsigned long));
    printf("size of float is:\t\t%ld bytes\n",sizeof(float));
    printf("size of double is:\t\t%ld bytes\n",sizeof(double));
    printf("\n");
    printf("size of char pointer is:\t%ld bytes\n",sizeof(char*));  // pointer is same as unsigned long !
    printf("size of int pointer is:\t\t%ld bytes\n",sizeof(int*));
    return 0;
}
```

Why I emphasize so much on the size? Check @Bintou's [二进制入门_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Th41167mM) instead!

### Basic Functions
What are functions?
**Something in, something out!** ~~(Garbage in, garbage out, see also [垃圾进，垃圾出 - 维基百科，自由的百科全书](https://zh.m.wikipedia.org/wiki/%E5%9E%83%E5%9C%BE%E8%BF%9B%EF%BC%8C%E5%9E%83%E5%9C%BE%E5%87%BA))~~
So what is the **in** part, and what is the **out** part



