---
aliases: [system call]
date created: Apr 4th, 2023
date modified: Apr 4th, 2023
---
Can be used in perf/latency measurement.

| # | Layer       | Components                                                            |
|---|-------------|-----------------------------------------------------------------------|
| 1 | Userspace   | user application                                                      |
| 2 | Userspace   | GNU C library (glibc)                                                 |
| - | ---         | ---                                                                   |
| 3 | Kernelspace | System Call Interface                                                 |
| 4 | Kernelspace | Subsystems: virtual filesystem, [[memory]] management, [[process]] management |
| 5 | Kernelspace | Architecture Dependent Code, device drivers                           |
| - | ---         | ---                                                                   |
| 6 | [[Hardware]]    | Physical devices                                                      |

