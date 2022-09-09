---
aliases: [TS]
tags: []
date created: Sep 4th, 2022
date modified: Sep 9th, 2022
---
## Overview
[TypeScript: Handbook - The TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)  
The goal of TypeScript is to be a static typechecker for JavaScript programs - in other words, a tool that runs before your code runs (static) and ensures that the types of the program are correct (typechecked).

## Type
### Optional Properties
[TypeScript: Documentation - Optional Properties](https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#optional-properties)  
Object types can also specify that some or all of their properties are _optional_. To do this, add a `?` after the property name:

```ts
function printName(obj: { first: string; last?: string }) {
  // ...
}
// Both OK
printName({ first: "Bob" });
printName({ first: "Alice", last: "Alisson" });

function printName(obj: { first: string; last?: string }) {
  // Error - might crash if 'obj.last' wasn't provided!
  console.log(obj.last.toUpperCase());
  
  // last is possibly 'undefined'.
  if (obj.last !== undefined) {
    // OK
    console.log(obj.last.toUpperCase());
  }
 
  // A safe alternative using modern JavaScript syntax:
  console.log(obj.last?.toUpperCase());
}
```

### Union Types
You can actually use a type alias to give a name to any type at all, not just an object type. For example, a type alias can name a union type:  
`type ID = number | string;`

### Type Assertions
``
___
[[TypeScript Config]]