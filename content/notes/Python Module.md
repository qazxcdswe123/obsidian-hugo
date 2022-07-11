---
title: Python Module
---
# Namespace
It turns out that we need to write `cs50.get_int(...)` when we import the entire library. This allows us to **namespace** functions, or keep their names in different spaces, with different prefixes. Then, multiple libraries with a `get_int` function won’t collide.

# import
[Docs](https://docs.python.org/3/tutorial/modules.html)
```python
>>> import fibo
>>> fibo.fib(1000)
>>> fibo.fib2(100)

>>> fibo.__name__
'fibo'
########
>>> from fibo import fib, fib2
>>> fib(500)
########

>>> from fibo import *
>>> fib(500)
```
This imports all names except those beginning with an underscore (`_`). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

[[Python sys]]