---
aliases: []
date created: Nov 24th, 2022
date modified: Apr 27th, 2023
---
Use cases: `asyncio` is often a perfect fit for [[IO]]-bound and high-level **structured** network code.

## `future`
A future is an object that represents a value that may not be available yet but will be at some point in the future.
Coroutines can await on `Future` objects until they either have a result or an exception set, or until they are cancelled

## Links
- [asyncio — Asynchronous I/O — Python 3.11.0 documentation](https://docs.python.org/3/library/asyncio.html)
- [PEP 492 – Coroutines with async and await syntax | peps.python.org](https://peps.python.org/pep-0492/#abstract)
- [[Python Magic Method]]
- [[JavaScript Event Loop]]
- [Futures and promises - Wikipedia](https://en.wikipedia.org/wiki/Futures_and_promises)