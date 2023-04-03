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

## Generics
```ts
function map<Input, Output>(arr: Input[], func: (arg: Input) => Output): Output[] {
  return arr.map(func);
}
 
// Parameter 'n' is of type 'string'
// 'parsed' is of type 'number[]'
const parsed = map(["1", "2", "3"], (n) => parseInt(n));
```

### Constraints
Generic functions can work on _any_ kind of value. Sometimes we want to relate two values, but can only operate on a certain subset of values. In this case, we can use a _constraint_ to limit the kinds of types that a type parameter can accept.

```ts
function longest<Type extends { length: number }>(a: Type, b: Type) {
  if (a.length >= b.length) {
    return a;
  } else {
    return b;
  }
}
 
// longerArray is of type 'number[]'
const longerArray = longest([1, 2], [1, 2, 3]);
// longerString is of type 'alice' | 'bob'
const longerString = longest("alice", "bob");

// Error! Numbers don't have a 'length' property
const notOK = longest(10, 100);
// Argument of type 'number' is not assignable to parameter of type '{ length: number; }'.

```

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
