---
aliases: []
date created: Apr 29th, 2023
date modified: Apr 29th, 2023
---

## Generator
Generators are iterators, a kind of iterable **you can only iterate over once**.  
Generators do not store all the values in memory, **they generate the values on the fly**:

```python
>>> mygenerator = (x*x for x in range(3))
>>> for i in mygenerator:
...    print(i)
0
1
4
```

Use `()` instead of `[]`. BUT, you **cannot** perform `for i in mygenerator` a second time since generators can only be used once: they calculate 0, then forget about it and calculate 1, and end calculating 4, one by one.

## Yield
`yield` is a keyword that is used like `return`, except the function will return a **generator**.

```python
>>> def create_generator():
...    mylist = range(3)
...    for i in mylist:
...        yield i*i
...
>>> mygenerator = create_generator() # create a generator
>>> print(mygenerator) # mygenerator is an object!
<generator object create_generator at 0xb7555c34>
>>> for i in mygenerator:
...     print(i)
0
1
4
```

## Links
- [[Python Iterator]]