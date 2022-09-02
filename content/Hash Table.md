[Wiki](https://en.wikipedia.org/wiki/Hash_table)
[4E](https://algs4.cs.princeton.edu/34hash/)

A hashtable works by taking the modulus of the hash over the number of buckets
if the constant used in the hash, and the number of buckets, are [coprime](https://math.stackexchange.com/a/64015), then collisions are minimised in some common cases. If they are not [coprime](https://math.stackexchange.com/a/64015), then there are some fairly simple relationships between inputs for which collisions are not minimised. All the hashes come out equal modulo the common factor, which means they'll all fall into the 1/n th of the buckets which have that value modulo the common factor. You get n times as many collisions, where n is the common factor.