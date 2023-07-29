---
aliases: []
date created: Jul 19th, 2023
date modified: Jul 28th, 2023
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

## Typescript
Use never

```ts
type Shape = Circle | Square;
 
function getArea(shape: Shape) {
  switch (shape.kind) {
    case "circle":
      return Math.PI * shape.radius ** 2;
    case "square":
      return shape.sideLength ** 2;
    default:
      const _exhaustiveCheck: never = shape;
      return _exhaustiveCheck;
  }
}
```