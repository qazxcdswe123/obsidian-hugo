---
aliases: []
date created: Jun 17th, 2023
date modified: Jun 17th, 2023
---

## What
A condition variable is an explicit [[queue]] that threads can put themselves on when some state of execution (i.e., some condition) is not as desired (by **waiting** on the condition)

## How
A condition variable has two operations associated with it: `wait()` and `signal()`.

The `wait()` call is executed when a [[thread]] wishes to put **itself** to sleep, hence allowing child threads to execute. The child will eventually run, and when it finishes executing, it will notify the parent thread by calling the `signal()` method.

The `signal()` call is executed when a thread has changed something in the program and thus wants to wake a sleeping thread that is waiting on this condition.

> TIP: ALWAYS HOLD THE [[Locks|LOCK]] WHILE SIGNALING
> Although it is strictly not necessary in all cases, it is likely simplest and best to hold the lock while signaling when using condition variables. The example above shows a case where you must hold the lock for correctness; however, there are some other cases where it is likely OK not to, but probably is something you should avoid. Thus, for simplicity, hold the lock when calling signal.
> The converse of this tip, i.e., hold the lock when calling wait, is not just a tip, but rather mandated by the semantics of wait, because wait always (a) assumes the lock is held when you call it, (b) releases said lock when putting the caller to sleep, and (c) re-acquires the lock just before returning. Thus, the generalization of this tip is correct: hold the lock when calling signal or wait, and you will always be in good shape.