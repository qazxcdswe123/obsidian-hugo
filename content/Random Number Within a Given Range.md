## What
Returning `rand() % N` does not uniformly give a number in the range `[0, N)`

## How
```c
#include <stdlib.h> // For random(), RAND_MAX

// Assumes 0 <= max <= RAND_MAX
// Returns in the closed interval [0, max]
long random_at_most(long max) {
  unsigned long
    // max <= RAND_MAX < ULONG_MAX, so this is okay.
    num_bins = (unsigned long) max + 1,
    num_rand = (unsigned long) RAND_MAX + 1,
    bin_size = num_rand / num_bins,
    defect   = num_rand % num_bins;

  long x;
  do {
   x = random();
  }
  // This is carefully written not to overflow
  while (num_rand - defect <= (unsigned long)x);

  // Truncated division is intentional
  return x/bin_size;
}
```

## Why


## Links
- [c - How to generate a random integer number from within a range - Stack Overflow](https://stackoverflow.com/questions/2509679/how-to-generate-a-random-integer-number-from-within-a-range)
- [[Hashtable]]