## `pipe`
```c
int pipe(int p[]) 
// Create a pipe, put read/write file descriptors in p[0] and p[1].
// p[0] is read fd, p[1] is write fd
```

- Writing data to one end of the pipe makes that data available for reading from the other end of the pipe. 
- Pipes provide a way for processes to communicate.

