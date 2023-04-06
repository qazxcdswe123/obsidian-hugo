---
aliases: []
date created: May 11th, 2022
date modified: Apr 5th, 2023
---
[Src](https://en.cppreference.com/w/cpp/language/override)  
[Stackoverflow]( https://stackoverflow.com/questions/29412412/does-final-imply-override)

> That's it. Now `override final` would simply mean  
> This function overrides a base class one (`override`) and cannot be overridden itself (`final`).“  
> `final` on it's own would impose a weaker requirement. `override` and `final` have independent behavior.

```cpp
#include <iostream>
 
struct A
{
    virtual void foo();
    void bar();
    virtual ~A();
};
 
// member functions definitions of struct A:
void A::foo() { [std::cout](http://en.cppreference.com/w/cpp/io/cout) << "A::foo();\n"; }
A::~A() { [std::cout](http://en.cppreference.com/w/cpp/io/cout) << "A::~A();\n"; }
 
struct B : A
{
//  void foo() const override; // Error: B::foo does not override A::foo
                               // (signature mismatch)
    void foo() override; // OK: B::foo overrides A::foo
//  void bar() override; // Error: A::bar is not virtual
    ~B() override; // OK: `override` can also be applied to virtual
                   // special member functions, e.g. destructors
    void override(); // OK, member function name, not a reserved keyword
};
 
// member functions definitions of struct B:
void B::foo() { [std::cout](http://en.cppreference.com/w/cpp/io/cout) << "B::foo();\n"; }
B::~B() { [std::cout](http://en.cppreference.com/w/cpp/io/cout) << "B::~B();\n"; }
void B::override() { [std::cout](http://en.cppreference.com/w/cpp/io/cout) << "B::override();\n"; }
 
int main() {
    B b;
    b.foo();
    b.override(); // OK, invokes the member function `override()`
    int override{42}; // OK, defines an integer variable
    [std::cout](http://en.cppreference.com/w/cpp/io/cout) << "override: " << override << '\n';
}
```

You will need a virtual to use override
