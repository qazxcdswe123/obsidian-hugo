---
aliases: [指针]
tags: Programming/C 
date created: Feb 13th, 2022
date modified: Oct 13th, 2022
---
## Basic Pointer
A pointer is a variable declared to store a memory address. Its declaration will also tell you the type of data it points to. You can retrieve the memory address of your variables, then mess with them.

To declare a pointer you can use `int *pt` or `int* pt`, note that these two syntax will do the same thing -- make a pointer pointing to type `int`. However, I personally prefer the first one since it indicates that **pt is a pointer, pointing to `int`**, the second one indicates that **pt is a int pointer**, which is certainly not the case.

The type `int` just tell the compiler how to read the data, for example, if you declare a variable with type `short` (which is 2 bytes), they just store binary data into memory and read exactly 2 bytes, we can typecast it to `int` can read 4 bytes next time(may lead to memory corruption though).

As a result, every pointer is 8 bytes(in 64 bits) since they refer to memory location, can read it with the type you specify. For example, `int *pt` means that `pt` is a location, read that location as `int`.

Also, `int *px, not_a_pointer;` is a common pitfall.

Now we know that pointer is nothing special but a memory location, location itself is not enough, to get the value inside the location, we need `*` again, however, this time we are not declaring pointers, we **dereference** it (memory is called reference), this means, we **set/get** value of it.

Pitfall comes again! We need to first make sure that it is pointing to a valid address!

```c
// BUGGY CODE START
int *x;
*x = 1;
// seg fault
// BUGGY CODE END

int var = 1;
int *pt = NULL; 
// initialize it with NULL so it won't mess useful address up
// The default value of a pointer is undefined

pt = &var;
// here we point pt to address of var

*pt = 2; // set value
// we change the value of that address, so now both var and *p is 2

printf("%d", var);
printf("%d", *pt); // get value
printf("%p\n", pt);
printf("%p\n", &var); // get address

// 2
// 2
// 0x16d10b26c
// 0x16d10b26c
```

In the example above, we use `&` to get the address of a variable, this is called **reference** a variable.  
`NULL` (in C) or `nullptr` (in C++) is a safe way to initialize a pointer, the former is a `int`, with value set to 0, the second is a pointer points to nothing

## More Than Basic
- Pointer arithmetic(If you were to design this, we would you do? Think about it!)
- Arrays are just pointer(since they are memory)
- Pointer to pointer(And more, aka 2d-array)
- `malloc` and `free`, `new` and `delete`, `new []` and `delete[]` (Best and basic practice)
- Memory is the key!
- `const` pointer
- Complex declaration: [cdecl: C gibberish ↔ English](https://cdecl.org/)

___

2022-07-28 Update  
其实要分辨指针，要（1）分清楚星号所在的地方，是个左值（left value），还是个右值（right value），（2）分清楚指针所指的类型，加上一些内存的通识就能理解了。

## General Pointer
- `*` 在 int 后还是数值前
> As far as C goes they both do the same thing. It is a matter of preference. `int* i` shows clearly that it is an int pointer type. `int *i` shows the fact that the asterisk only affects a single variable. So `int *i, j` and `int* i, j` would both create `i` as an int pointer and `j` as an int.

`int *i, j` 和 `int* i, j` 效果都一样，一个指针和一个整数

- 两指针可以相减，不可相加。若要进行相减运算，则两指针必须指向同一数组，相减结果为相距的数组元素个数
___

## Pointer to Function
URL: [How do function pointers in C work? - Stack Overflow](https://stackoverflow.com/questions/840501/how-do-function-pointers-in-c-work)
- Use Case

```c
int (*functionPtr)(int,int);
functionPtr = &addInt;

int add2to3(int (*functionPtr)(int, int)) {
    return (*functionPtr)(2, 3);
}
// function as argument
```

- Via typedef

```c
typedef int (*myFuncDef)(int, int);
// note that the typedef name is indeed myFuncDef

myFuncDef functionFactory(int n) {
    printf("Got parameter %d", n);
    myFuncDef functionPtr = &addInt;
    return functionPtr;
}
```