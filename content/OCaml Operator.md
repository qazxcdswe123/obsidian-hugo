## equal
- There are two equality operators in OCaml, `=` and `==`, with corresponding inequality operators `<>` and `!=`. Operators `=` and `<>` examine _structural_ equality whereas `==` and `!=` examine _physical_ equality.
- [OCaml library : Stdlib](https://ocaml.org/api/Stdlib.html)

## prefix operator
```ocaml
( + ) 3 4;;
let add3 = ( + ) 3
```