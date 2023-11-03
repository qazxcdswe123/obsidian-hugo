The deferred call's arguments are **evaluated immediately**, but the function call is not executed until the **surrounding function returns**.  

Deferred function calls are pushed onto a [[stack]].

The expression must be a function or method call; it cannot be parenthesized. Calls of built-in functions are restricted as for [expression statements](https://go.dev/ref/spec#Expression_statements).

Good for resources cleanup.