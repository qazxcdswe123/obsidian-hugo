---
aliases: []
link:
  - "[[Pointer]]"
  - "[[Rust Smart Pointer]]"
date created: Nov 15th, 2022
date modified: Aug 1st, 2023
---

## Overview
- defined in the `std` namespace in the [`<memory>`](https://learn.microsoft.com/en-us/cpp/standard-library/memory?view=msvc-170) header file.  
They are crucial to the [RAII](https://learn.microsoft.com/en-us/cpp/cpp/object-lifetime-and-resource-management-modern-cpp?view=msvc-170) or _[[RAII|Resource Acquisition Is Initialization]]_ programming idiom.

## `unique_ptr`
A `unique_ptr` has exclusive ownership of the object it points to.

```cpp
unique_ptr<T> name(new T(args));

name.reset(); // Free the memory before we exit function block.
```

## `shared_ptr`
Use reference counter, used when you want to assign one raw pointer to multiple owners. The raw pointer is not deleted until all `shared_ptr` owners have gone out of scope or have otherwise given up ownership.

It use extra size: 2 pointers, one for object and one for the shared control block that contains the reference count.
- [std::shared\_ptr - cppreference.com](https://en.cppreference.com/w/cpp/memory/shared_ptr)

## `weak_ptr`
provides access to an object that is owned by one or more `shared_ptr` instances, but does not participate in reference counting.

Use when you want to observe an object, but do not require it to remain alive. Required in some cases to break circular references between `shared_ptr` instances.

## Comparison
- Difference Between `unique_ptr` and `shared_ptr`  
We can only have 1 `unique_ptr` but we can have multiple `shared_ptr`. However, `shared_ptr` may introduce some small overhead.