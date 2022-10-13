---
aliases: []
tags: []
date created: Aug 12th, 2022
date modified: Aug 12th, 2022
---
## Const
![](https://img.ynchen.me/2022/10/92123767a39e7835cf57a84e836730c9.webp)

[`const` is a contract – Arthur O'Dwyer – Stuff mostly about C++](https://quuxplusone.github.io/blog/2019/01/03/const-is-a-contract/)
Should not be modified

## Constexpr
URL: [constexpr (C++) | Microsoft Docs](https://docs.microsoft.com/en-us/cpp/cpp/constexpr-cpp?view=msvc-170)

Like const, it can be applied to variables: A compiler error is raised when any code attempts to modify the value. Unlike const, constexpr can also be applied to functions and class constructors. constexpr indicates that the value, or return value, is constant and, where possible, is computed at compile time.

It means constant expression. Like const, it can be applied to variables: A compiler error is raised when any code attempts to modify the value.

 Unlike const, constexpr can also be applied to functions and class constructors. constexpr indicates that the value, or return value, is constant and, where possible, is computed at compile time.
> function and constructor, compute at compile time

The primary difference between const and constexpr variables is that the initialization of a const variable can be deferred until run time. A constexpr variable must be initialized at compile time.  All constexpr variables are const.

A constexpr variable or function must return a literal type.

A constexpr function is one whose return value is computable at compile time when consuming code requires it. Consuming code requires the return value at compile time to initialize a constexpr variable, or to provide a non-type template argument.

A constexpr function or constructor is implicitly inline.

When its arguments are constexpr values, a constexpr function produces a compile-time constant. When called with non-constexpr arguments, or when its value isn't required at compile time, it produces a value at run time like a regular function. (This dual behavior saves you from having to write constexpr and non-constexpr versions of the same function.)

It can't be virtual. A constructor can't be defined as constexpr when the enclosing class has any virtual base classes.

