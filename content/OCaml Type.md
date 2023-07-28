## Checking
```ocaml
(123 : int);;
- : int = 33

(33 : bool);;
Error: This expression has type int but an expression was expected of type bool
```

## `int`
- Range from $-2^{62}$ to $2^{62} - 1$
- one bit is used at runtime ([[Garbage Collector]]) to distinguish int from pointers
- [OCaml library : Int64](https://ocaml.org/api/Int64.html)
- [GitHub - ocaml/Zarith: The Zarith library implements arithmetic and logical operations over arbitrary-precision integers and rational numbers. The implementation, based on GMP, is very efficient.](https://github.com/ocaml/Zarith)

## `float`
- `int_of_float`
- `float_of_int`

## `char`
- `char_of_int`
- `int_of_char`

## `string`
- concatenation: `^`
- `"abc".[0]`

## `type variable`
- or generic/polymorphic
- `'a`: unknown type

## `type` variant
```ocaml
type t1 = C | D
type t2 = D | E
let x = D

type t = C1 [of t1] | ... | Cn [of tn]


type node = {value : int; next : mylist}
	and mylist = Nil | Node of node


type 'a mylist = Nil | Cons of 'a * 'a mylist

let rec length : 'a mylist -> int = function
  | Nil -> 0
  | Cons (_, t) -> 1 + length t

let empty : 'a mylist -> bool = function
  | Nil -> true
  | Cons _ -> false
```

Provide a type-safe way of doing something that might before have seemed impossible.
Variant types may mention their own name inside their own body

### Polymorphic Variants
1. You don’t have declare their type or constructors before using them.
2. There is no name for a polymorphic variant type. (So another name for this feature could have been “anonymous variants”.)
3. The constructors of a polymorphic variant start with a backquote character.

```ocaml
let f = function
  | 0 -> `Infinity
  | 1 -> `Finite 1
  | n -> `Finite (-n)
```