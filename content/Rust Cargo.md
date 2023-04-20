---
aliases: []
date created: Nov 12th, 2022
date modified: Nov 12th, 2022
---
- We can create a project using `cargo new`.
- We can build a project using `cargo build`.
- We can build and run a project in one step using `cargo run`.
	- `cargo run -- searchstring example-filename.txt`
	- two hyphens to indicate the following arguments are for our program rather than for `cargo`
- We can build a project without producing a binary to check for errors using `cargo check`.
- Instead of saving the result of the build in the same directory as our code, Cargo stores it in the _target/debug_ directory.
- `cargo build --release` to build optimized version.