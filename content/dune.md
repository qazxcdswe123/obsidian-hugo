Build system for [[OCaml]]

## Init

```
# in dune
(executable
 (name hello))
 
# in dune-project
(lang dune 3.9)
```

This _project_ file is needed in the root directory of every source tree that you want to compile with Dune. In general, you’ll have a `dune` file in every subdirectory of the source tree but only one `dune-project` file at the root.

## Build
```
dune build hello.exe

dune exec ./hello.exe

dune clean
```

