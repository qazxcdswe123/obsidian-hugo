```ocaml
# let average a b =
    (a +. b) /. 2.0;; (* +. /. to do floating point arithmetic *)
val average : float -> float -> float = <fun>

f : arg1 -> arg2 -> ... -> argn -> rettype

let rec even n =
  n = 0 || odd (n - 1)
and odd n =
  n <> 0 && even (n - 1)
```

## Pipe
- `|>`
- `e1 |> e2` is just another way of writing `e2 e1`

## Labeled Arguments
```ocaml
let f ~name1:arg1 ~name2:arg2 = arg1 + arg2;;
let f ~name1:name1 ~name2:name2 = name1 + name2
let f ~name1 ~name2 = name1 + name2

let f ~name1:(arg1 : int) ~name2:(arg2 : int) = arg1 + arg2

(* Optional Argument *)
let f ?name:(arg1=8) arg2 = arg1 + arg2
```
