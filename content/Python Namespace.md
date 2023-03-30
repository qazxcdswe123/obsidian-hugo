---
aliases: []
tags: []
date created: Jul 8th, 2022
date modified: Aug 12th, 2022
---
## LEGB Rules
URL: [Namespaces and Scope in Python – Real Python](https://realpython.com/python-namespaces-scope/)

In a Python program, there are four types of namespaces: (Searched in sequence)
- Local: If you refer to x inside a function, then the interpreter first searches for it in the innermost scope that’s local to that function.
- Enclosing: If x isn’t in the local scope but appears in a function that resides inside another function, then the interpreter searches in the enclosing function’s scope.
- Global: If neither of the above searches is fruitful, then the interpreter looks in the global scope next.
- Built-in: If it can’t find x anywhere else, then the interpreter tries the built-in scope.

This is the LEGB rule as it’s commonly called in Python literature (although the term doesn’t actually appear in the Python documentation). The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope

### Global VS Nonlocal
- Global  
Access var defined outside function
- Nonlocal  
Access var defined in closure function

## Example

```python
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

After local assignment: test spam
After nonlocal assignment: nonlocal spam
After global assignment: nonlocal spam
In global scope: global spam
```

`nonlocal` works in nested structure

