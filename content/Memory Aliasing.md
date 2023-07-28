---
aliases: []
date created: Jul 23rd, 2023
date modified: Jul 23rd, 2023
---
Two pointers point to the same chunk of [[memory]], preventing the compiler from doing certain optimizations.

## Example
```c
void foo(int *array, int *size, int *value) {
    for(int i = 0; i < *size; ++i) {
        array[i] = 2 * (*value);
    }
}
```

`*value` could be an alias for an element of the array it could change on any given iteration.

## Links
- [c++ - What is the strict aliasing rule? - Stack Overflow](https://stackoverflow.com/questions/98650/what-is-the-strict-aliasing-rule)
- [c++ - What is aliasing and how does it affect performance? - Stack Overflow](https://stackoverflow.com/questions/9709261/what-is-aliasing-and-how-does-it-affect-performance)
- [What is Strict Aliasing and Why do we Care? · GitHub](https://gist.github.com/shafik/848ae25ee209f698763cffee272a58f8)