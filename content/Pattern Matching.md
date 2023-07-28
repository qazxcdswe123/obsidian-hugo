---
aliases: []
date created: Jul 19th, 2023
date modified: Jul 19th, 2023
---

## OCaml

```ocaml
let rec sum = function
  | [] -> 0
  | h :: t -> h + sum t

match List.hd [] with
  | [] -> "empty"
  | _ :: _ -> "nonempty"
  | exception (Failure s) -> s
```