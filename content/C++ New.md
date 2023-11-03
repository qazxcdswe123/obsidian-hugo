---
aliases: []
date created: Apr 7th, 2022
date modified: Sep 7th, 2022
---
- [StackOverflow](https://stackoverflow.com/questions/620137/do-the-parentheses-after-the-type-name-make-a-difference-with-new)

```cpp
struct A { int m; }; // POD
struct B { ~B(); int m; }; // non-POD, compiler generated default ctor
struct C { C() : m() {}; ~C(); int m; }; // non-POD, default-initialising m
```

In a [[C++]]03 conformant [[compiler]], things should work like so:
- `new A` - indeterminate value
- `new A()` - value-initialize A, which is zero-initialization since it's a POD.
- `new B` - default-initializes (leaves B::m uninitialized)
- `new B()` - value-initializes B which zero-initializes all fields since its default ctor is compiler generated as opposed to user-defined.
- `new C` - default-initializes C, which calls the default ctor.
- `new C()` - value-initializes C, which calls the default ctor.

`new Thing();` is explicit that you want a constructor called whereas `new Thing;` is taken to imply you don't mind if the constructor isn't called.  
`new Thing();` is explicit that you want a constructor called whereas `new Thing;` is taken to imply you don't mind if the constructor isn't called.

If used on a struct/class with a user-defined constructor, there is no difference. If called on a trivial struct/class (e.g. `struct Thing { int i; };`) then `new Thing;` is like `malloc(sizeof(Thing));` whereas `new Thing();` is like `calloc(sizeof(Thing));` - it gets zero initialized.
