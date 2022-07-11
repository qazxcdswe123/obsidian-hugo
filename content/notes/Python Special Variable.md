---
title: Python Special Variable
---
Source: [https://stackoverflow.com/questions/419163/what-does-if-name-main-do](https://stackoverflow.com/questions/419163/what-does-if-name-main-do)
## Special Variables
When the Python interpreter reads a source file, it first defines a few special variables. 
In this case, we care about the `__name__` variable.
**When Your Module Is the Main Program**
If you are running your module (the source file) as the main program, e.g.
```python
python foo.py
```
the interpreter will assign the hard-coded string `"__main__"` to the `__name__` variable, i.e.
```python
# It's as if the interpreter inserts this at the top
# of your module when run as the main program.
__name__ = "__main__" 
```
**When Your Module Is Imported By Another**
On the other hand, suppose some other module is the main program and it imports your module. This means there's a statement like this in the main program, or in some other module the main program imports:
```python
# Suppose this is in some other main program.
import foo
```
It will assign the name `"foo"` from the import statement to the `__name__` variable, i.e.
```python
# It's as if the interpreter inserts this at the top
# of your module when it's imported from another module.
__name__ = "foo"
```