---
aliases: []
date created: Jul 31st, 2022
date modified: Apr 8th, 2023
---
- [[False Sharing]]
- [[Memory Aliasing]]

## Speculative Execution
With speculative execution, the operations are evaluated, but the final results are not stored in the program registers or data [[memory]] until the processor can be certain that these instructions should actually have been executed.

## Eliminate write/read Dependency
the outcome of a memory read depends on a recent [[memory]] write.  
[[Cache]]

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
In [computer science](https://en.wikipedia.org/wiki/Computer_science "Computer science"), **[[CPU Instruction]] pipelining** is a technique for implementing [instruction-level parallelism](https://en.wikipedia.org/wiki/Instruction-level_parallelism "Instruction-level parallelism") within a single processor. Pipelining attempts to keep every part of the processor busy with some [[CPU Instruction]] by dividing incoming [instructions](https://en.wikipedia.org/wiki/Machine_code "Machine code") into a series of sequential steps (the eponymous "[pipeline](https://en.wikipedia.org/wiki/Pipeline_(computing) "Pipeline (computing)")") performed by different [processor units](https://en.wikipedia.org/wiki/Central_processing_unit#Structure_and_implementation "Central processing unit") with different parts of instructions processed in parallel.

A key feature of pipelining is that it increases the throughput of the system (i.e., the number of customers served per unit time), but it may also slightly increase the latency

## Resources
- [Software optimization resources. C++ and assembly. Windows, Linux, BSD, Mac OS X](https://www.agner.org/optimize/)
- [Herb Sutter @ NWCPP: Machine Architecture: Things Your Programming Language Neve - YouTube](https://www.youtube.com/watch?v=L7zSU9HI-6I)
- [Slides about memory optimization by Christer Ericson](https://web.archive.org/web/20160422113037/http://www.research.scea.com/research/pdfs/GDC2003_Memory_Optimization_18Mar03.pdf) 
- LWN.net's article ["_What every programmer should know about memory_"](http://lwn.net/Articles/250967/)