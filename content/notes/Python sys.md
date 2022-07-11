---
title: Python sys
---
[Src](https://docs.python.org/3/tutorial/modules.html#executing-modules-as-scripts)
[Docs](https://docs.python.org/3/library/sys.html)

# Example Usage
When you run a Python module with
`python fibo.py <arguments>`
the code in the module will be executed, just as if you imported it, but with the `__name__` set to `"__main__"`. That means that by adding this code at the end of your module:
```
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
```
you can make the file usable as a script as well as an importable module, because the code that parses the command line only runs if the module is executed as the “main” file:
```
python fibo.py 50
0 1 1 2 3 5 8 13 21 34
```
