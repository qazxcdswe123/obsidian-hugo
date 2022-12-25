---
aliases: []
tags: []
date created: Dec 24th, 2022
date modified: Dec 24th, 2022
---

## What
> It was designed to move objects, whose lifetime expires, instead of copying them. The data is transferred from one object to another. In most cases, the data transfer does not move this data physically in memory. It helps to avoid expensive copying.

When the argument is a temporary value stored in [[Memory|heap]], it will be automatically `delete` after it goes out of the scope. By using `std::move` and 

## How
To implement it, [rvalue references](https://pvs-studio.com/en/blog/terms/6517/), move constructors, and the move assignment operator were added. Also, some functions were added to the STL to support move semantics. For example, _[std::move](https://pvs-studio.com/en/blog/terms/6518/)_ and _[std::forward](https://pvs-studio.com/en/blog/terms/6515/)_.

```c++
#include <utility>
template <typename T>
void Swap(T &lhs, T &rhs) noexcept
{
	T t = std::move(lhs);
	lhs = std::move(rhs);
	rhs = std::move(t); 
}
```

## Why
- Turning expensive copies into cheap moves.
- Implementing safe "move-only" types; that is, types for which copying does not make sense, but moving does. Examples include locks, file handles, and smart pointers with unique ownership semantics.

```c++
std::vector<int> arrA(1'000'000, 0);
std::vector<int> arrB(1'000'000, 1);
Swap(arrA, arrB);
```

Two objects of the _`std::vector<int>`_ type are created. Each contains 1'000'000 elements. Then the _Swap_ function swaps them. The _std::vector_ class template contains a non-trivial copy constructor that has the following functions:

- performs dynamic memory allocation to the desired number of elements;
- makes a deep copy of the elements from the passed _std::vector_.

As a result, we have 3'000'000 copies of _int_ type objects. The situation may get even worse if _std::vector_ is instantiated by a [non-trivially copied](https://en.cppreference.com/w/cpp/named_req/TriviallyCopyable) type.

## Links
- [c++ - What is move semantics? - Stack Overflow](https://stackoverflow.com/questions/3106110/what-is-move-semantics/11540204#11540204)