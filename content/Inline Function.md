[What does it mean to inline a function and how does it affect a program?](https://www.ibm.com/support/pages/what-does-it-mean-inline-function-and-how-does-it-affect-program)
# General
An inline function is one for which the [[compiler]] copies the code from the function definition directly into the code of the calling function rather than creating a separate set of instructions in [[memory]]. This eliminates call-linkage overhead and can expose significant [[optimization]] opportunities. Using the "inline" specifier is only a suggestion to the [[compiler]] that an inline expansion can be performed; the [[compiler]] is free to ignore the suggestion.

# [[C]]
[c++ - When should I write the keyword 'inline' for a function/method? - Stack Overflow](https://stackoverflow.com/questions/1759300/when-should-i-write-the-keyword-inline-for-a-function-method)
`inline` is more like `static` or `extern` than a directive telling the [[compiler]] to inline your functions. `extern`, `static`, `inline` are linkage directives, used almost exclusively by the linker, not the [[compiler]].


