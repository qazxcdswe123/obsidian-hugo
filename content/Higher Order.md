## `map`

## `fold_left` and `fold_right`
- They combine list elements in opposite orders, as indicated by their names. Function `fold_right` combines from the right to the left, whereas `fold_left` proceeds from the left to the right.
- Function `fold_left` is **tail recursive**, whereas `fold_right` is not.
- The types of the functions are different.

```ocaml
let rec fold_left f accu l =
  match l with
    [] -> accu
  | a::l -> fold_left f (f accu a) l
  
let rec fold_right f l accu =
  match l with
    [] -> accu
  | a::l -> f a (fold_right f l accu)

- : ('a -> 'b -> 'a) -> 'a -> 'b list -> 'a = <fun>
- : ('a -> 'b -> 'b) -> 'a list -> 'b -> 'b = <fun>
```

## `for_all`