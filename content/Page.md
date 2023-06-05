## What
A typical size of page is 4kb (4096 bytes, $2^{12}$ bytes)  
For the [[virtual memory]] address, we split it into 2 parts, `index` and `offset`, `index` for page and `offset` for byte in page, so the size of `offset` is 12 bits, and `index` is 3 `9bit` numbers (L2, L1, L0) in RISC-V. Each memory access need 3 memory lookups and it's expensive, so we use TLB to cache recently used address.

## Links
- [[Replacement Policy]]