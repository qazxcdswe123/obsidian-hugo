---
aliases: [FP]
date created: Mar 3rd, 2023
date modified: Jul 17th, 2023
---
- [[OOP]]

## Functional
- [[OCaml]]
- [[Scheme]]
- [[Rust]]
- [[C++]]
- [[ReactJS]]

> Programming in a functional style often includes using functions as values by passing them in arguments, returning them from other functions, assigning them to variables for later execution, and so forth.
> Adapting to that perspective requires letting go of old ideas: assignment statements, loops, classes and objects, among others. That won’t be easy.
> 
> A function maps an input to an output; for the same input, it always produces the same output. That is, mathematical functions are _stateless_: they do not maintain any extra information or _state_ that persists between usages of the function. 
> Functions are _first-class_: you can use them as input to other functions, and produce functions as output. Expressing everything in terms of functions enables a uniform and simple programming model that is easier to reason about than the procedures and methods found in other families of languages.

- No mutable data (no side effect).
- No state (no implicit, hidden state).
- **All state is bad?** No, the **hidden**, **implicit** state is bad.
- Functional programming does not eliminate state, it just makes it **visible** and **explicit** (at least when programmers want it to be).
- Functions are _pure_ functions in the mathematical sense: their output depend only on their inputs, there is no “environment”.
- The same result returned by functions called with the same inputs.

### Properties
- [[Pattern Matching]]
- _Closures_, a function-like construct you can store in a variable
- _Iterators_, a way of processing a series of elements

## Example
```ocaml
let rec fast_fib n =
  let rec helper i pp p = 
    if i = 0 then pp
    else helper (i - 1) (pp + p) p
  in
  if n = 0 then 0 
  else helper n 0 1
```

- [[Rust Functional Programming]]
- [[Higher Order]]
- [[Monad]]