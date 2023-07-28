---
aliases: []
date created: Jun 6th, 2023
date modified: Jul 18th, 2023
---
- [[OCaml Type]]
- [[OCaml Functions]]
- [[OCaml Operator]]
- [[OCaml Module]]
- [[dune]]

## Expression

```ocaml
# let a = 1 in
  let b = 2 in
    a + b;;
- : int = 3

# 2.0 *. 3.14;;
- : float = 6.28
```


## Assertions
The expression `assert e` evaluates `e`. If the result is `true`, nothing more happens, and the entire expression evaluates to a special value called _unit_. The unit value is written `()` and its type is `unit`. But if the result is `false`, an exception is raised.

## Links
- [[Functional Programming]]