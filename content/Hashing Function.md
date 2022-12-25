## Naive
```c
unsigned long hash_function(char* str) {
    unsigned long i = 0;
    for (int j=0; str[j]; j++)
        i += str[j];
    return i % CAPACITY;
}
```

## MD5

## SHA

## Fibonacci Hash

- [Fibonacci Hashing: The Optimization that the World Forgot (or: a Better Alternative to Integer Modulo) | Probably Dance](https://probablydance.com/2018/06/16/fibonacci-hashing-the-optimization-that-the-world-forgot-or-a-better-alternative-to-integer-modulo/)