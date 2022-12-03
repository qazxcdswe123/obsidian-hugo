---
aliases: []
tags: []
date created: Nov 23rd, 2022
date modified: Nov 23rd, 2022
---
> The NP-complete problems are the “hardest” in NP. Informally, a problem is NP-complete if it satisfies two conditions: (1) it’s in NP and (2) if a polynomial-time algorithm exists for the problem, then there is a way to convert every problem in NP into this problem in such a way as to solve them all in polynomial time. If a polynomial-time algorithm exists for any NP-complete problem—that is, if any NP-complete problem is in P—then P D NP. Because NP-complete problems are the hardest in NP, if it turns out that any problem in NP is not polynomial-time solvable, then none of the NP-complete problems are. A problem is NP-hard if it satisfies the second condition for NP-completeness but may or may not be in NP.

- `P`: problems solvable in polynomial time, i.e., we can solve the problem in time polynomial in the size of the input to the problem.
- `Certificate`: a proposed solution to a problem.
- `NP`: problems verifiable in polynomial time, i.e., given a certificate, we can verify that the certificate is a solution the problem in time polynomial in the size of the input to the problem and the size of the certificate.
- `NP-hard`: a problem such that if there is a polynomial-time algorithm to solve this problem, then we can convert every problem in NP into this problem in such a way to solve every problem in NP in polynomial time.
- `NP-complete`: a problem that is NP-hard and also in NP.