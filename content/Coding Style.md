# Pocket - 15-213/15-513 Intro to Computer Systems: Code Style
URL: https://getpocket.com/read/225087580

Good code should be mostly self-documenting: your variable names and function calls should generally make it clear what you are doing. Comments should not describe what the code does, but why; what the code does should be self-evident. (Assume the reader knows C better than you do when you consider what is self-evident.)
> Why not what

File header: Each file should contain a comment describing the purpose of the file and how it fits in to the larger project. This is also a good place to put your name and email address.
> Purpose

Large blocks of code: If a block of code is particularly long, a comment at the top can help the reader know what to expect as they're reading it, and let them skip it if it's not relevant.
> long code

Function header: Each function should be prefaced with a comment describing the purpose of the function (in a sentence or two), the function's arguments and return value, any error cases that are relevant to the caller, any pertinent side effects, and any assumptions that the function makes.
> argument, return value, error handling, assumptions

Tricky bits of code: If there's no way to make a bit of code self-evident, then it is acceptable to describe what it does with a comment. In particular, pointer arithmetic is something that often deserves a clarifying comment.
> tricky hack

You should use \#define to clarify the meaning of magic numbers. In the above example, doing "#define BUFLEN 256" and then using the "BUFLEN" constant in both the declaration of "buf" and the call to "fgets".
> magic number use define

If you allocate memory (malloc, calloc), you should free it after use. Your program should not have memory leaks. If you use open a file, you should close it after use. Closing a file is very important, especially with output files. The reason is that output is often buffered.
> Close file

