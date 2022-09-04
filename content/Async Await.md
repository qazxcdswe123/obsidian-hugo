---
aliases: []
tags: []
date created: Apr 3rd, 2022
date modified: Aug 25th, 2022
---
See also [[Asynchronous]] and [[JavaScript Event Loop]]
# Javascript
src: [Nodejs doc](https://nodejs.dev/learn/modern-asynchronous-javascript-with-async-and-await)  

**async/await is built on [[JavaScript promise]]**.  
They make the code look like it's synchronous, but it's **asynchronous** and **non-blocking** behind the scenes.

The one caveat being, anything you `await` must have been declared `async`: