---
aliases: []
date created: Jul 13th, 2022
date modified: Apr 8th, 2023
---
- [[Git Command]]
- [[Git Hacks]]
- [[Git Tag]]

## Git Object
At its core, Git is a “content-addressed filesystem”. That means that unlike regular filesystems, where the name of a file is arbitrary and unrelated to that file’s contents, **the names of files as stored by Git are mathematically derived from their contents**. 
This has a very important implication: if a single byte of, say, a text file, changes, its internal name will change, too. To put it simply: you don’t _modify_ a file, you create a new file in a different location. Objects are just that: files in the git repository, whose path is determined by their contents.

### Thin Pack
A thin pack is a pack file that contains deltas that reference base objects that are not contained within the pack, but are known to exist at the receiving end
This can significantly reduce network traffic during transfer, but it requires the receiving end to know how to "thicken" these packs by adding the missing base objects to the pack

___

- [[Lazygit]]
