## What
When you write source code, you access the library through an API. Once the code is compiled, your application accesses the binary data in the library through the ABI.
The ABI defines the structures and methods that your compiled application will use to access the external library (just like the API did), only on a lower level.
Your API defines the order in which you pass arguments to a function. Your ABI defines the mechanics of _how_ these arguments are passed (registers, stack, etc.).

## Links
- [compiler construction - What is an application binary interface (ABI)? - Stack Overflow](https://stackoverflow.com/questions/2171177/what-is-an-application-binary-interface-abi)