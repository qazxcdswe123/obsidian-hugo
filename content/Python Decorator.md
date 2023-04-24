## Decorator
A function returning another function, usually applied as a function transformation using the `@wrapper` syntax. Common examples for decorators are [`classmethod()`](https://docs.python.org/3/library/functions.html#classmethod "classmethod") and [`staticmethod()`](https://docs.python.org/3/library/functions.html#staticmethod "staticmethod").

It was inspired in part by [Java annotations](https://en.wikipedia.org/wiki/Java_annotation "Java annotation"), and have a similar syntax; the decorator syntax is pure [syntactic sugar](https://en.wikipedia.org/wiki/Syntactic_sugar "Syntactic sugar"), using `@` as the keyword:

```python
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
```

## Links
- [Python Docs](https://docs.python.org/3/glossary.html#term-decorator)
- [Python syntax and semantics - Wikipedia](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators)