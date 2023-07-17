## Setup
```bash
brew install minimal-racket
raco pkg install racket-langserver
```

## Evaluation
### Applicative Order Evaluation
Also known as eager evaluation or strict evaluation, function's arguments are evaluated before the function is applied.

A significant effect of applicative order evaluation is that recursive functions may not terminate if an argument to a function is recursive and must be evaluated before calling the function

### Normal Order Evaluation
Also known as lazy evaluation, evaluation of procedure arguments is delayed until the actual argument values are needed

In other words, arguments are passed as-is to the procedure, and the leftmost outermost function application is always evaluated first
