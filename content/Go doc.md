## Packages
Every package should have a package comment introducing the package. It provides information relevant to the package as a whole and generally sets expectations for the package.

```
// Package path implements utility routines for manipulating slash-separated
// paths.
//
// The path package should only be used for paths separated by forward
// slashes, such as the paths in URLs. This package does not deal with
// Windows paths with drive letters or backslashes; to manipulate
// operating system paths, use the [path/filepath] package.
package path
```

## Links
- [Go Doc Comments - The Go Programming Language](https://tip.golang.org/doc/comment)