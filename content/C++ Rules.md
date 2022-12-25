---
aliases: []
tags: []
date created: Dec 24th, 2022
date modified: Dec 24th, 2022
---

## Rules of 3
If a class requires a user-defined [destructor](https://en.cppreference.com/w/cpp/language/destructor "cpp/language/destructor"), a user-defined [copy constructor](https://en.cppreference.com/w/cpp/language/copy_constructor "cpp/language/copy constructor"), or a user-defined [copy assignment operator](https://en.cppreference.com/w/cpp/language/as_operator "cpp/language/as operator"), it almost certainly requires all three.

## Rules of 5
A user-defined (or `= default` or `= delete` declared) destructor, copy-constructor, or copy-assignment operator prevents implicit definition of the [move constructor](https://en.cppreference.com/w/cpp/language/move_constructor "cpp/language/move constructor") and the [move assignment operator](https://en.cppreference.com/w/cpp/language/move_operator "cpp/language/move operator"), any class for which move semantics are desirable, has to declare all five special member functions:

## Copy and Swap Idiom
Definition: Use copy constructor to create a copy of the old data called `temp`, and `swap` the new data and old data. The temporary copy then destructs, so the old data will gone. The new data lives.
In order to use the copy-and-swap idiom, we need three things: a working copy-constructor, a working destructor (both are the basis of any wrapper, so should be complete anyway), and a `swap` function.
A swap function is a _non-throwing_ function that swaps two objects of a class, member for member. We might be tempted to use `std::swap` instead of providing our own, but this would be impossible; `std::swap` uses the copy-constructor and copy-assignment operator within its implementation, and we'd ultimately be trying to define the assignment operator in terms of itself!
- [[C++ Move Semantics]]

## Links
- [The rule of three/five/zero - cppreference.com](https://en.cppreference.com/w/cpp/language/rule_of_three)
- [c++ - What is the copy-and-swap idiom? - Stack Overflow](https://stackoverflow.com/questions/3279543/what-is-the-copy-and-swap-idiom)