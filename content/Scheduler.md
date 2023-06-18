## Scheduler
- First Come First Serve (FCFS)
	- automatically executes queued requests and processes in order of their arrival
- Shortest Job First (SJF)
- Shortest Time-to-Completion First
- Multi-Level Feedback [[Queue]]
	- Idea
		- If a [[process]] uses too much CPU time, it will be moved to a lower-priority queue.
		- If a process is I/O-bound or an interactive process, it will be moved to a higher-priority queue.
		- If a process is waiting too long in a low-priority queue and [starving](https://en.wikipedia.org/wiki/Starvation_(computer_science) "Starvation (computer science)"), it will be [aged](https://en.wikipedia.org/wiki/Aging_(scheduling) "Aging (scheduling)") to a higher-priority queue.
	- Rules
		- Rule 1: If Priority(A) > Priority(B), A runs (B doesn’t).
		- Rule 2: If Priority(A) = Priority(B), A & B run in round-robin fashion using the time slice (quantum length) of the given queue.
		- Rule 3: When a job enters the system, it is placed at the highest priority (the topmost queue).
		- Rule 4: Once a job uses up its time allotment at a given level (regardless of how many times it has given up the CPU), its priority is reduced (i.e., it moves down one queue).
		- Rule 5: After some time period S, move all the jobs in the system to the topmost queue.
- Proportional-share Scheduling
- Completely Fair Scheduler (CFS)
	- CFS basically models an “ideal, precise multi-tasking CPU” on real [[hardware]].

