[[Python Built-in Functions]]
# parameters
[Src](https://docs.python.org/3/tutorial/controlflow.html#special-parameters)
- `\` Positional-Only Parameters
	- Positional-only parameters are placed before a `/` (forward-slash). The `/` is used to logically separate the positional-only parameters from the rest of the parameters.
- `*` Keyword-Only Arguments
	- To mark parameters as _keyword-only_, indicating the parameters must be passed by keyword argument, place an `*` in the arguments list just before the first _keyword-only_ parameter.

```python
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)

>>> pos_only_arg(1)
1

>>> kwd_only_arg(arg=3)
3

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3
```

## Function Annotations
[Src](https://docs.python.org/3/tutorial/controlflow.html#function-annotations)
[Annotations](https://docs.python.org/3/glossary.html#term-function-annotation) are stored in the `__annotations__` attribute of the function as a dictionary and have no effect on any other part of the function. Parameter annotations are defined by a colon after the parameter name, followed by an expression evaluating to the value of the annotation. Return annotations are defined by a literal `->`, followed by an expression, between the parameter list and the colon denoting the end of the [`def`](https://docs.python.org/3/reference/compound_stmts.html#def) statement. The following example has a required argument, an optional argument, and the return value annotated:
```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

