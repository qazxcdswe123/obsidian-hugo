## `Result` Type
### `Ok`
`Ok` variant indicates the operation was successful, and inside `Ok` is the successfully generated value.

### `Err`
`Err` variant means the operation failed, and `Err` contains information about how or why the operation failed.

An instance of `Result` has an [`expect` method](https://doc.rust-lang.org/std/result/enum.Result.html#method.expect) that you can call. If this instance of `Result` is an `Err` value, `expect` will cause the program to crash and display the message that you passed as an argument to `expect`. If the `read_line` method returns an `Err`, it would likely be the result of an error coming from the underlying operating system. If this instance of `Result` is an `Ok` value, `expect` will take the return value that `Ok` is holding and return just that value to you so you can use it.