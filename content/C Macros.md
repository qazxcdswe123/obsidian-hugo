---
aliases: []
date created: Aug 15th, 2022
date modified: Sep 21st, 2022
---
From K&R  
![](https://img.ynchen.me/2022/08/aa82d39c3dc10878bf4e9f7eb0df7412.png)

![](https://img.ynchen.me/2022/08/def0ddeb8a7978ab23b09bbed4fd3849.png)

- Use `#` as replacement text  
![](https://img.ynchen.me/2022/08/9373ea21c02642ae1e7680a3d36dd908.png)

- And Use `##` to concatenate  
The preprocessor operator `##` provides a way to concatenate actual arguments during macro expansion.If a parameter in the replacement text is adjacent to a ##the parameter is replaced by the actual argument, the `##` and surrounding white space are removed, and the result is re-scanned.For example, the macro paste concatenates its two arguments:  
`#define paste(front, back) front ## back`

Nonetheless, macros are valuable.One practical example comes from `<stdio.h>`, in which `getchar` and `putchar` are often defined as macros to avoid the e run-time overhead of a function call per character processed.The functions in `<ctype.h>` are also usually implemented as macros.
