---
aliases: []
date created: Oct 5th, 2022
date modified: Mar 13th, 2023
---
> **Rule**: When possible, use the type parameter itself rather than constraining it  
> **Rule**: Always use as few type parameters as possible  
> **Rule**: If a type parameter only appears in one location, strongly reconsider if you actually need it  
> When writing a function type for a callback, _never_ write an optional parameter unless you intend to _call_ the function without passing that argument

## Signatures

### Call Signatures
In [[JavaScript]], functions can have properties in addition to being callable. However, the function type expression syntax doesn’t allow for declaring properties. If we want to describe something callable with properties, we can write a _call signature_ in an object type:

```ts
type DescribableFunction = {
  description: string;
  (someArg: number): boolean;
};
function doSomething(fn: DescribableFunction) {
  console.log(fn.description + " returned " + fn(6));
}
```

### Construct Signatures
[[JavaScript]] functions can also be invoked with the `new` operator. [[TypeScript]] refers to these as _constructors_ because they usually create a new object. You can write a _construct signature_ by adding the `new` keyword in front of a call signature:

```ts
type SomeConstructor = {
  new (s: string): SomeObject;
};
function fn(ctor: SomeConstructor) {
  return new ctor("hello");
}
```

The parenthesis is for argument, it is actually a function.

- [[Typescript Generics]]

## Function Overloads
```ts
function makeDate(timestamp: number): Date;
function makeDate(m: number, d: number, y: number): Date;
function makeDate(mOrTimestamp: number, d?: number, y?: number): Date {
  if (d !== undefined && y !== undefined) {
    return new Date(y, mOrTimestamp, d);
  } else {
    return new Date(mOrTimestamp);
  }
}
const d1 = makeDate(12345678);
const d2 = makeDate(5, 5, 5);
```

- Always prefer parameters with union types instead of overloads when possible
