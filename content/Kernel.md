- [[ebpf]]

# Header File
A header file is a file containing C declarations and macro definitions to be shared between several source files. You request the use of a header file in your program by including it, with the C preprocessing directive `#include`.

Linux-image is the kernel binary. Linux headers is the source header files. There's no reason to include them together, debian keeps dev packages and binary package separate. You only need the headers package if you need to build something that uses kernel functions