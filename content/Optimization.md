---
aliases: [Pipeline]
tags: [CSAPP, ] 
date created: Jul 31st, 2022
date modified: Aug 16th, 2022
---
[[CSAPP]]
# Life in the Real World: Performance Improvement Techniques
- High-level design
High-level design, Choose appropriate algorithms and data structures for the problem at hand. Be especially vigilant to avoid algorithms or coding techniques that yield asymptotically poor performance.

- Eliminate excessive function calls
Eliminate excessive function calls, Move computations out of loops when possible. Consider selective compromises of program modularity to gain greater efficiency.

- Eliminate unnecessary memory references
Eliminate unnecessary memory references, Introduce temporary variables to hold intermediate results. Store a result in an array or global variable only when the final value has been computed.

- Low-level optimizations
Low-level optimizations, Structure code to take advantage of the hardware capabilities.
Unroll loops to reduce overhead and to enable further optimizations.
Find ways to increase instruction-level parallelism by techniques such as multiple accumulators and reassociation.
Rewrite conditional operations in a functional style to enable compilation via conditional data transfers.
## Memory Aliasing
The case where two pointers may designate the same [[memory]] location is known as [[memory]] aliasing.  
Two variable point to the same chunk of [[memory]].

### Eliminating Unneeded Memory References
Use temporary variable in loop so there's no heavy [[memory]] [[IO]].

## Speculative Execution
With speculative execution, the operations are evaluated, but the final results are not stored in the program registers or data [[memory]] until the processor can be certain that these instructions should actually have been executed.

## Eliminate write/read Dependency
the outcome of a memory read depends on a recent [[memory]] write.

### Loop Unrolling

```c
for (int i=0; i<n-3; i+=4)  // note the n-3 bound for starting i + 0..3
{
  sum1 += data[i+0];
  sum2 += data[i+1];
  sum3 += data[i+2];
  sum4 += data[i+3];
}
sum = sum1 + sum2 + sum3 + sum4;
// if n%4 != 0, handle final 0..3 elements with a rolled up loop or whatever
```

In general, we have found that unrolling a loop and accumulating multiple values in parallel is a more reliable way to achieve improved program performance.

## Pipelining
In [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"), **[[instruction]] pipelining** is a technique for implementing [instruction-level parallelism](https://en.wikipedia.org/wiki/Instruction-level_parallelism "Instruction-level parallelism") within a single processor. Pipelining attempts to keep every part of the processor busy with some [[instruction]] by dividing incoming [instructions](https://en.wikipedia.org/wiki/Machine_code "Machine code") into a series of sequential steps (the eponymous "[pipeline](https://en.wikipedia.org/wiki/Pipeline_(computing) "Pipeline (computing)")") performed by different [processor units](https://en.wikipedia.org/wiki/Central_processing_unit#Structure_and_implementation "Central processing unit") with different parts of instructions processed in parallel.

A key feature of pipelining is that it increases the throughput of the system (i.e., the number of customers served per unit time), but it may also slightly increase the latency
