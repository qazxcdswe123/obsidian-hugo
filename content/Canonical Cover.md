---
aliases: []
date created: May 21st, 2023
date modified: May 21st, 2023
---
used in database systems to reduce the complexity of checking functional dependencies while updating the database

1. No functional dependency in the canonical cover contains an extraneous attribute.
2. Each left side of a functional dependency in the canonical cover is unique.

For example, let's find the canonical cover for the set of functional dependencies F = {A -> BC, B -> AC, C -> AB}:

1. Decompose FDs: F = {A -> B, A -> C, B -> A, B -> C, C -> A, C -> B}
2. Remove redundant FDs: F = {A -> B, A -> C, B -> A, C -> A}
3. Combine the final set of FDs: Canonical cover = {A -> BC, B -> A, C -> A}