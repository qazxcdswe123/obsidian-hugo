---
aliases: []
date created: Apr 12th, 2023
date modified: Apr 12th, 2023
---

## Design
1. A compact and versatile data structure for indexing terms, providing lookup by exact match, prefix match, and fuzzy match.
2. An API layer on top of this data structure, providing the search features.

## Data Structure
- The radix tree minimizes the memory footprint of the index, because common prefixes are stored only once, and nodes are compressed into a single multi-character node whenever possible.
- Radix trees offer fast key lookup, with performance proportional to the key length, and fast lookup of subtrees sharing the same key prefix. These properties make it possible to offer performant exact match and prefix search.
- On top of a radix tree it is possible to implement lookup of keys that are within a certain maximum edit distance from a given key. This search rapidly becomes complex as the maximum distance grows, but for practical search use-cases the maximum distance is small enough for this algorithm to be performant. Other more performant solutions for fuzzy search would require more space (e.g. n-gram indexes).

## Links
- [[tokenizer]]
- [[Inverted Index]]