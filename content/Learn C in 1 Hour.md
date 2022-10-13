---
aliases: []
tags: [] 
date created: Oct 11th, 2022
date modified: Oct 13th, 2022
---
# Learn C in 1 Hour
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
	- Syntax
		- It is what it is!
	- Everything that I consider 谭浩强 related
		- Don't learn from it, get a new book instead! See [The Definitive C Book Guide and List - Stack Overflow](https://stackoverflow.com/questions/562303/the-definitive-c-book-guide-and-list) and [c++ faq - The Definitive C++ Book Guide and List - Stack Overflow](https://stackoverflow.com/questions/388242/the-definitive-c-book-guide-and-list)
		- i++++i
		- etc. (Just too many...)
	- **Details** (Will be partially covered in this text)
	- Compilation

## Building Blocks
How a program was constructed?
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

Use this syntax to defined variables, then we can use these variables to build bigger program later on.

```c
// \t for tab
// \n for new line
// include here so we can use printf
// if you are usnig cpp, use <cstdio> or <iostream>
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

Why I (and also @Tover) emphasize so much on the size? Check @Bintou's [二进制入门_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Th41167mM) to see why!

___

And some basic operators:

```c
// Increment and decrement operators:
int j = 0;
int s = j++; // Return j THEN increase j. (s = 0, j = 1)
s = ++j; // Increase j THEN return j. (s = 2, j = 2)
// same with j-- and --j

// Bitwise operators!
~0x0F; // => 0xFFFFFFF0 (bitwise negation, "1's complement", example result for 32-bit int)
0x0F & 0xF0; // => 0x00 (bitwise AND)
0x0F | 0xF0; // => 0xFF (bitwise OR)
0x04 ^ 0x0F; // => 0x0B (bitwise XOR)
0x01 << 1; // => 0x02 (bitwise left shift (by 1))
0x02 >> 1; // => 0x01 (bitwise right shift (by 1))
```

___

A common pitfall for new C programmers is that variables may be casted implicitly, for example.

```c
float a = 1 / 10;
// what will a be?

printf("lf\n", 1.0 / 10);
double one = 1;
printf("%lf\n", ans);
double ans = one / 10;
// how about this one?

int i1 = 1, i2 = 2;
float f1 = 1.0, f2 = 2.0;
// You need to cast at least one integer to float to get a floating-point result
(float)i1 / i2; // => 0.5f
i1 / (double)i2; // => 0.5 // Same with double
f1 / f2; // => 0.5, plus or minus epsilon
```

### Conditions and Loops
We need conditions and loops to things more than calculation.

```c
// Comparison operators are probably familiar
// there is no Boolean type in C, but there is one in C++.
// Here we use ints instead.
// 0 is false, anything else is true. (The comparison
// operators always yield 0 or 1.)
3 == 2; // => 0 (false)
3 != 2; // => 1 (true)
3 > 2;  // => 1
3 < 2;  // => 0
2 <= 2; // => 1
2 >= 2; // => 1

// C is not Python - comparisons do NOT chain.
// Warning: The line below will compile, but it means `(0 < a) < 2`.
// This expression is always true, because (0 < a) could be either 1 or 0.
// In this case it's 1, because (0 < 1).
int between_0_and_2 = 0 < a < 2;
// Instead use:
int between_0_and_2 = 0 < a && a < 2;

// Logic works on ints
// result will only be 1 and 0
!3; // => 0 (Logical not)
!0; // => 1

1 && 1; // => 1 (Logical and)
0 && 1; // => 0
0 || 1; // => 1 (Logical or)
0 || 0; // => 0

// Conditional ternary expression ( ? : )
// Readability is the key!
int e = 5;
int f = 10;
int z;
z = (e > f) ? e : f; // => 10 "if e > f return e, else return f."
```

Here comes the real-world conditions:

```c
// While loops exist
int ii = 0;
while (ii < 10) { //ANY value less than ten is true.
  printf("%d, ", ii++); // ii++ increments ii AFTER using its current value.
} // => prints "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "

int kk = 0;
do {
  printf("%d, ", kk);
} while (++kk < 10); // ++kk increments kk BEFORE using its current value.
// => prints "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "

// For loops too
int jj;
for (jj = 0; jj < 10; jj++) {
  printf("%d, ", jj);
} // => prints "0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "
// or equivalantly
for (int jj = 0; jj < 10; jj++) {
  printf("%d, ", jj);
}

// we can think of it
for (initialization; condition; post) {
	// for body here
}

// Most common condition: if
if (0) {
  printf("I am never run\n");
} else if (0) {
  printf("I am also never run\n");
} else {
  printf("I print\n");
}

// less common condition: switch
// branching with multiple choices: switch()
switch (a) {
case 0: // labels need to be integral *constant* expressions (such as enums)
  printf("Hey, 'a' equals 0!\n");
  break; // if you don't break, control flow falls over labels
case 1:
  printf("Huh, 'a' equals 1!\n");
  break;
  // Be careful - without a "break", execution continues until the
  // next "break" is reached.
case 3:
case 4:
  printf("Look at that.. 'a' is either 3, or 4\n");
  break;
default:
  // if `some_integral_expression` didn't match any of the labels,
  // handle the error
  cleanUp();
  exit(-1);
  break;
}

// Question: Is all these interchangeable?
// This is left as an exercise(stupidly simple)

---

// *****NOTES*****:
// Loops and Functions MUST have a body. If no body is needed:
int i;
for (i = 0; i <= 5; i++) {
  ; // use semicolon to act as the body (null statement)
}
// Or
for (i = 0; i <= 5; i++);
```

![](https://img.ynchen.me/2022/10/74217e52affe01cd790e077dbc232cf4.webp)

### Basic Functions
What are functions?  
**Something in, something out!** (Garbage in, garbage out, see also [垃圾进，垃圾出 - 维基百科，自由的百科全书](https://zh.m.wikipedia.org/wiki/%E5%9E%83%E5%9C%BE%E8%BF%9B%EF%BC%8C%E5%9E%83%E5%9C%BE%E5%87%BA))  
So what is the **in** part, and what is the **out** part

```c
return_type function_name (argument_type argument_name) {
	function body
	return return_value;
}
// what is in, what is out?

// for example
int main(int argc, char** argv) {
	return 0; // what is the return value here?
}

// You can provide default arguments for a function
// if they are not provided by the caller.

void doSomethingWithInts(int a = 1, int b = 4)
{
	int tmp = a;
	a = b;
	b = tmp;	
	// will this work?
}
// void function return nothing

doSomethingWithInts();      // a = 1,  b = 4
doSomethingWithInts(20);    // a = 20, b = 4
doSomethingWithInts(20, 5); // a = 20, b = 5
```

 Let's see some examples
 
 ```c 
#include <stdio.h>

// calculate n!
void factorial(int n)
{ 
    int result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }
    printf("%i! = %i\n", n, result);
}
// What's the problem here?


int factorial_iterative(int n)
{
    int result = 1;
    for (int i = 1; i <= n; i++)
    {
        result *= i;
    }
    return result;
}

int factorial_bad(int n)
{
    return n * factorial_bad(n - 1);
}

int factorial_recursize(int n)
{
	// base case
    if (n == 1) // what about n = 0
    {
        return 1;
    }
    else
    {
        return n * factorial_recursize(n - 1);
    }
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Recursion: Factorial of %d is %d\n", n, factorial_recursize(n));
    printf("Iteration: Factorial of %d is %d\n", n, factorial_iterative(n));
    return 0;
}
```
 
Let's see one more example of recursion.

```c
int fibo(int n)
{
    if (n == 0)
    {
        return 0;
    }
    else if (n == 1)
    {
        return 1;
    }
    else
    {
        return fibo(n - 1) + fibo(n - 2);
    }
}
```

See also: [[Recursion]] [[todo]]

## Memory
### Data Revisited
One variable at a time is not enough, we need something to store lots of variable(which leads to a chunk of memory).

Here `array` comes in handy

```c
type array_name[size] = {initial_value};

// Arrays must be initialized with a concrete size.
char my_char_array[20]; // This array occupies 1 * 20 = 20 bytes
int my_int_array[20]; // This array occupies 4 * 20 = 80 bytes

// You can initialize an array of twenty ints that all equal 0 thusly:
int my_array[20] = {0};
// where the "{0}" part is called an "array initializer".
// All elements (if any) past the ones in the initializer are initialized to 0:
int my_array[5] = {1, 2};
// So my_array now has five elements, all but the first two of which are 0: 
// [1, 2, 0, 0, 0]
// NOTE that you get away without explicitly declaring the size 
// of the array IF you initialize the array on the same line:
int my_array[] = {0};
// NOTE that, when not declaring the size, the size of the array is the number 
// of elements in the initializer. With "{0}", my_array is now of size one: [0]
// To evaluate the size of the array at run-time, divide its byte size by the
// byte size of its element type:
int my_array_size = sizeof(my_array) / sizeof(my_array[0]);
// WARNING You should evaluate the size *before* you begin passing the array 
// to functions (see later discussion) because arrays get "downgraded" to 
// raw pointers when they are passed to functions (so the statement above 
// will produce the wrong result inside the function).

// Indexing an array is like other languages -- or,
// rather, other languages are like C
my_array[0]; // => 0

// Arrays are mutable; it's just memory!
my_array[1] = 2;
printf("%d\n", my_array[1]); // => 2

// Strings are just arrays of chars terminated by a NULL (0x00) byte,
// represented in strings as the special character '\0'.
// (We don't have to include the NULL byte in string literals; the compiler
//  inserts it at the end of the array for us.)
char a_string[20] = "This is a string";

// Question1: What is a_string[19]?
// Question2: char b_string[5] = "abcde"; What's wrong here?

printf("%s\n", a_string); // %s formats a string

printf("%d\n", a_string[16]); // => 0
// i.e., byte #17 is 0 (as are 18, 19, and 20)

// Multi-dimensional arrays:
int multi_array[2][5] = {
  {1, 2, 3, 4, 5},
  {6, 7, 8, 9, 0}
};
// access elements:
int array_int = multi_array[0][2]; // => 3
```

Question: If I told you `array` is just chunk of memory, how would you design an `array`, or more specifically, a `2d array`?

[[Pointer]]

### Function Revisited
- Pass by reference/value
Assume we want to change 2 variable

```c
#include <stdio.h>

void badSwap(int a, int b) {
  int temp = a;
  a = b;
  b = temp;
}

void swapTwoNumbers(int *a, int *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int main(int argc, char *argv[]) {
  int a = 1, b = 2;
  badSwap(a, b);
  printf("a = %d, b = %d\n", a, b);
  swapTwoNumbers(&a, &b);
  printf("a = %d, b = %d\n", a, b);
  return 0;
}
```

What's the difference?

It turns out that function argument are passed by value, we simply copy them(make a copy) to the function, so when inside `badSwap` we are only manipulating the copy not the real value! (Why we do that? Think about it!)

The correct way is to pass a pointer to the variable to be change! This is time we are changing the value of the address(address get copied but the address don't get changed), so we are fine.

Note that there is also a `C++` version of swap(won't work on `C`)! For more details, see 
[pointers - Pass by reference in C for swapping function - Stack Overflow](https://stackoverflow.com/a/73925857/12614515)
[pointers - Passing by reference in C - Stack Overflow](https://stackoverflow.com/questions/2229498/passing-by-reference-in-c)

```cpp
void swap(int &a, int &b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}
```

In `C`, pass by reference is only a illusion!
- Question: How to return an array?

___

## Aside
### Typecasting

```c
// Every value in C has a type, but you can cast one value into another type
// if you want (with some constraints).

int x_hex = 0x01; // You can assign vars with hex literals
                  // binary is not in the standard, but allowed by some
                  // compilers (x_bin = 0b0010010110) 

// Casting between types will attempt to preserve their numeric values
printf("%d\n", x_hex); // => Prints 1
printf("%d\n", (short) x_hex); // => Prints 1
printf("%d\n", (char) x_hex); // => Prints 1

// If you assign a value greater than a types max val, it will rollover
// without warning.
printf("%d\n", (unsigned char) 257); // => 1 (Max char = 255 if char is 8 bits long)

// For determining the max value of a `char`, a `signed char` and an `unsigned char`,
// respectively, use the CHAR_MAX, SCHAR_MAX and UCHAR_MAX macros from <limits.h>

// Integral types can be cast to floating-point types, and vice-versa.
printf("%f\n", (double) 100); // %f always formats a double...
printf("%f\n", (float)  100); // ...even with a float.
printf("%d\n", (char)100.0);
```  

See also: [[Programming Language]]