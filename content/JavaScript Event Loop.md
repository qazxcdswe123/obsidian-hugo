---
aliases: []
tags: []
date created: Sep 3rd, 2022
date modified: Sep 3rd, 2022
---
[[Async Await]]
[[JavaScript promise]]
[The event loop - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/EventLoop)

## Runtime Concept
### [[Memory|Heap]]
Objects are allocated in a [[Memory|heap]] which is just a name to denote a large (mostly unstructured) region of [[memory]].

### [[Queue]]
A JavaScript runtime uses a message [[queue]], which is a list of messages to be processed. Each message has an associated function that gets called to handle the message.  
function is called with the message as an input parameter.

## Event Loop
### Messages

```js
while (queue.waitForMessage()) {
  queue.processNextMessage();
}
```

This offers some nice properties when reasoning about your program, including the fact that whenever a function runs, it cannot be preempted and will run entirely before any other code runs (and can modify data the function manipulates). This differs from [[C++]], for instance, where if a function runs in a [[thread]], it may be stopped at any point by the runtime system to run some other code in another [[thread]].

A good practice to follow is to make message processing short and if possible cut down one message into several messages.

### Adding Messages
If there is no other message in the queue, and the stack is empty, the message is processed right after the delay. However, if there are messages, the `setTimeout` message will have to wait for other messages to be processed. For this reason, the second argument indicates a _minimum_ time — not a _guaranteed_ time.
