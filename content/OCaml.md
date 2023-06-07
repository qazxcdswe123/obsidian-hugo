## Expression
```ocaml
# let a = 1 in
  let b = 2 in
    a + b;;
- : int = 3
```

## Functions
```ocaml
# let average a b =
    (a +. b) /. 2.0;; (* +. /. to do floating point arithmetic *)
val average : float -> float -> float = <fun>

f : arg1 -> arg2 -> ... -> argn -> rettype
```