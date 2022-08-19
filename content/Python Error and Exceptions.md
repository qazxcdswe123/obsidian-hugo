---
aliases: []
tags: [] 
date created: Jul 24th, 2022
date modified: Aug 16th, 2022
---
[[C++ error handling]]
[Src](https://docs.python.org/3/tutorial/errors.html)

# Exceptions Handling
An exception is thrown when a fundamental assumption of the current code block is found to be false.
`Try, catch, and finally` statements enable the use of a resource, catching any possible exceptions and then releasing the resource in the final block, making sure that there are no memory leaks.

## Try Clause
[Built-in Exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
```

The [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement works as follows.
-   First, the _try clause_ (the statement(s) between the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) and [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) keywords) is executed.
-   If no exception occurs, the _except clause_ is skipped and execution of the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement is finished.
-   If an exception occurs during execution of the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) clause, the rest of the clause is skipped. Then, if its type matches the exception named after the [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) keyword, the _except clause_ is executed, and then execution continues after the try/except block.
-   If an exception occurs which does not match the exception named in the _except clause_, it is passed on to outer [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statements; if no handler is found, it is an _unhandled exception_ and execution stops with a message as shown above.
-  An _except clause_ may name multiple exceptions as a parenthesized tuple, for example:  
	`except (RuntimeError, TypeError, NameError):`

The [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) … [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) statement has an optional _else clause_, which, when present, must follow all _except clauses_.  
It is useful for code that must be executed if the _try clause_ does not raise an exception. For example:

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

The use of the `else` clause is better than adding additional code to the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) clause because it avoids accidentally catching an exception that wasn’t raised by the code being protected by the `try` … `except` statement

### Example

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

## Exception Chaining
[Src](https://docs.python.org/3/tutorial/errors.html#exception-chaining)

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

## Finally Clause
[Src](https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions)  
The `finally` clause will execute as the last task before the [`try`](https://docs.python.org/3/reference/compound_stmts.html#try) statement completes. The `finally` clause runs whether or not the `try` statement produces an exception.
-   If an exception occurs during execution of the `try` clause, the exception may be handled by an [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) clause. If the exception is not handled by an `except` clause, the exception is re-raised after the `finally` clause has been executed.
-   An exception could occur during execution of an `except` or `else` clause. Again, the exception is re-raised after the `finally` clause has been executed.
-   If the `finally` clause executes a [`break`](https://docs.python.org/3/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue) or [`return`](https://docs.python.org/3/reference/simple_stmts.html#return) statement, exceptions are not re-raised.
-   If the `try` statement reaches a [`break`](https://docs.python.org/3/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3/reference/simple_stmts.html#continue) or [`return`](https://docs.python.org/3/reference/simple_stmts.html#return) statement, the `finally` clause will execute just prior to the `break`, `continue` or `return` statement’s execution.
-   If a `finally` clause includes a `return` statement, the returned value will be the one from the `finally` clause’s `return` statement, not the value from the `try` clause’s `return` statement.

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

As you can see, the [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause is executed in any event. The [`TypeError`](https://docs.python.org/3/library/exceptions.html#TypeError "TypeError") raised by dividing two strings is not handled by the [`except`](https://docs.python.org/3/reference/compound_stmts.html#except) clause and therefore re-raised after the `finally` clause has been executed.  
In real world applications, the [`finally`](https://docs.python.org/3/reference/compound_stmts.html#finally) clause is useful for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.

## User-defined Exceptions
[Src](https://docs.python.org/3/tutorial/errors.html#user-defined-exceptions)  
Programs may name their own exceptions by creating a new exception class (see [Classes](https://docs.python.org/3/tutorial/classes.html#tut-classes) for more about Python classes).  
Exceptions should typically be derived from the [`Exception`](https://docs.python.org/3/library/exceptions.html#Exception "Exception") class, either directly or indirectly.  
More on [[Python Class OOP]]
