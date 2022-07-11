---
title: Lambda and Anonymous Function
---
> In computer programming, an anonymous function (function literal, lambda abstraction, lambda function, lambda expression or block) is a function definition that is not bound to an identifier. [Wikipedia](https://en.wikipedia.org/wiki/Anonymous_function)
> Use lambda functions when an anonymous function is required for a short period of time.
> has no name but takes in some argument or arguments, and returns a value immediately.

Bound to variable but not identifier, no parentheses or `return` keyword
# Example
## [[C++]]
In C++11 and later, a lambda expression—often called a lambda—is a convenient way of defining an anonymous function object (a closure) right at the location where it's invoked or passed as an argument to a function.
Typically lambdas are used to encapsulate a few lines of code that are passed to algorithms or asynchronous functions.

[MSDN](https://docs.microsoft.com/en-us/cpp/cpp/lambda-expressions-in-cpp?view=msvc-170)
`[capture](parameters) -> return_type { function_body }`
![](https://s2.loli.net/2022/07/08/voRHn3ZxE9u7WPi.png)
1.  _capture clause_ (Also known as the _lambda-introducer_ in the C++ specification.)
2.  _parameter list_ Optional. (Also known as the _lambda declarator_)
3.  _mutable specification_ Optional.
4.  _exception-specification_ Optional.
5.  _trailing-return-type_ Optional.
6.  _lambda body_.

## [[Python]]
`<Function_Name> = lambda <Paramater_List>: <Expression>`
```python
>>> foo = lambda x: x * x
>>> foo(10)
100
```
