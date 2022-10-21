---
aliases: []
tags: []
date created: Oct 21st, 2022
date modified: Oct 21st, 2022
---
- **Don’t call Hooks inside loops, conditions, or nested functions**
- **Only Call Hooks from React Functions**
- State updates are batched!

To update a component with new data, two things need to happen:

1. **Retain** the data between renders.
2. **Trigger** React to render the component with new data (re-rendering).

```js
<button onClick={() => {
setNumber(number + 1);
setNumber(number + 1);
setNumber(number + 1);
}}>+3</button>

setNumber(0 + 1);
setNumber(0 + 1);
setNumber(0 + 1);
```

The [`useState`](https://beta.reactjs.org/apis/react/useState) Hook provides those two things:

1. A **state variable** to retain the data between renders.
2. A **state setter function** to update the variable and trigger React to render the component again.

When using [[React Component#Function Component]], it is updated with [[React Hooks]]