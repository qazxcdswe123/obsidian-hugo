---
aliases: []
tags: []
date created: Mar 13th, 2023
date modified: Mar 14th, 2023
---

## Overview
> In TypeScript, just as in ECMAScript 2015, any file containing a top-level `import` or `export` is considered a module.
> 
> Conversely, a file without any top-level import or export declarations is treated as a script whose contents are available in the global scope (and therefore to modules as well).
> 
> Modules are executed within their own scope, not in the global scope. This means that variables, functions, classes, etc. declared in a module are not visible outside the module unless they are explicitly exported using one of the export forms. Conversely, to consume a variable, function, class, interface, etc. exported from a different module, it has to be imported using one of the import forms.

## Export All as `x`
```ts
export * as utilities from "./utilities";

import { utilities } from "./index";
```

## `export =` And `import = require`
When exporting a module using `export =`, TypeScript-specific `import module = require("module")` must be used to import the module.

## `import` Brackets
[javascript - When should I use curly braces for ES6 import? - Stack Overflow](https://stackoverflow.com/questions/36795819/when-should-i-use-curly-braces-for-es6-import)

## Import Image
[javascript - TS2307: Cannot find module './images/logo.png' - Stack Overflow](https://stackoverflow.com/questions/57127606/ts2307-cannot-find-module-images-logo-png)
```ts
declare module '*.png' {
  const value: any
  export = value
}
```

## Links
- [TypeScript: Documentation - Modules](https://www.typescriptlang.org/docs/handbook/modules.html)