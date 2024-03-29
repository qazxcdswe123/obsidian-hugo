---
aliases: []
link:
  - "[[C++]]"
date created: Nov 18th, 2022
date modified: Aug 1st, 2023
---
## C++ Lambda
In C++11 and later, a lambda expression—often called a lambda—is a convenient way of defining an anonymous function object (a [[closure]]) right at the location where it's invoked or passed as an argument to a function.  

- [MSDN](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-170)  
- `[capture](parameters) -> return_type { function_body }`  
![](https://s2.loli.net/2022/07/08/voRHn3ZxE9u7WPi.png)
1. _capture clause_ (Also known as the _lambda-introducer_ in the C++ specification.)
2. _parameter list_ Optional. (Also known as the _lambda declarator_)
3. _mutable specification_ Optional.
4. _exception-specification_ Optional.
5. _trailing-return-type_ Optional.
6. _lambda body_.

Capture clause
```
[] it means that you will not provide anything to give to lambda.
[&] it is used to say that you have some references to mess with.
[=] it is used to make the copy.
[this] is used to the enclosing class.
```