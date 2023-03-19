---
aliases: []
tags: []
date created: Sep 9th, 2022
date modified: Mar 15th, 2023
---

### No Implicit Any -`noImplicitAny`
[TypeScript: TSConfig Reference - Docs on every TSConfig option](https://www.typescriptlang.org/tsconfig/#noImplicitAny)  
Recall that in some places, TypeScript doesn’t try to infer types for us and instead falls back to the most lenient type: `any`. This isn’t the worst thing that can happen - after all, falling back to `any` is just the plain JavaScript experience anyway.

However, using `any` often defeats the purpose of using TypeScript in the first place. The more typed your program is, the more validation and tooling you’ll get, meaning you’ll run into fewer bugs as you code. Turning on the [`noImplicitAny`](https://www.typescriptlang.org/tsconfig#noImplicitAny) flag will issue an error on any variables whose type is implicitly inferred as `any`.

### Source Map -`sourceMap`
[TypeScript: TSConfig Reference - Docs on every TSConfig option](https://www.typescriptlang.org/tsconfig#sourceMap)

### Strict Null Checks -`strictNullChecks`
[TypeScript: TSConfig Reference - Docs on every TSConfig option](https://www.typescriptlang.org/tsconfig#strictNullChecks)
## Environment `include`
Add environment variable to project by changing `include`  in `tsconfig`
