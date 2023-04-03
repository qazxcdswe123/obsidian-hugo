---
aliases: []
date created: Feb 6th, 2023
date modified: Feb 6th, 2023
---
- [`System.exit(int status)`](http://java.sun.com/javase/6/docs/api/java/lang/System.html#exit(int)) - Equivalent to `Runtime.getRuntime().exit(status)`
- [`Runtime.exit(int status)`](http://java.sun.com/javase/6/docs/api/java/lang/Runtime.html#exit(int)) - Terminates the currently running JVM by initiating its shutdown sequence (run all registered [shutdown hooks](http://java.sun.com/javase/6/docs/api/java/lang/Runtime.html#addShutdownHook(java.lang.Thread)), and [uninvoked finalizers](http://java.sun.com/javase/6/docs/api/java/lang/Runtime.html#runFinalizersOnExit(boolean)), if necessary). Once this is done the JVM halts.
- [`Runtime.halt(int status)`](http://java.sun.com/javase/6/docs/api/java/lang/Runtime.html#halt(int)) - Forcibly terminates the currently running JVM.
