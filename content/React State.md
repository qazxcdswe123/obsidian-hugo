---
aliases: []
tags: []
date created: Oct 21st, 2022
date modified: Nov 16th, 2022
---
## Cavets
- **Don’t call Hooks inside loops, conditions, or nested functions**
- **Only Call Hooks from React Functions**
- State updates are batched!
- States are immutable

To update a component with new data, two things need to happen:
1. **Retain** the data between renders.
2. **Trigger** React to render the component with new data (re-rendering).  

## Immutable State
You should **treat any [[JavaScript object]] that you put into state as read-only.** Or it may not be updated by React Correctly  

In [[JavaScript]], arrays are just another kind of object. [Like with objects](https://beta.reactjs.org/learn/updating-objects-in-state), **you should treat arrays in React state as read-only.**  
This means that you shouldn’t reassign items inside an array like `arr[0] = 'bird'`, and you also shouldn’t use methods that mutate the array, such as `push()` and `pop()`.  
Instead, every time you want to update an array, you’ll want to pass a _new_ array to your state setting function. To do that, you can create a new array from the original array in your state by calling its non-mutating methods like `filter()` and `map()`. Then you can set your state to the resulting new array.

- When you store objects in state, mutating them will not trigger renders and will change the state in previous render “snapshots”.
- Instead of mutating an object, create a _new_ version of it, and trigger a re-render by setting state to it.

In general, **you should only mutate objects that you have just created.** If you were inserting a _new_ artwork, you could mutate it, but if you’re dealing with something that’s already in state, you need to make a copy.

```js
<button onClick={() => {
setNumber(number + 1);
setNumber(number + 1);
setNumber(number + 1);
}}>+3</button>

setNumber(0 + 1);
setNumber(0 + 1);
setNumber(0 + 1);

// state for object
const nextArtwork = { ...person.artwork, city: 'New Delhi' };  
const nextPerson = { ...person, artwork: nextArtwork };  
setPerson(nextPerson);

// state for array
// add with spread
setArtists([
  { id: nextId++, name: name },
  ...artists // Put old items at the end
]);

// delete with filter
setArtists(
  artists.filter(a => a.id !== artist.id)
);

// transform with map
function handleClick() {
  const nextShapes = shapes.map(shape => {
    if (shape.type === 'square') {
	  // No change
	  return shape;
    } else {
	  // Return a new circle 50px below
	  return {
	    ...shape,
	    y: shape.y + 50,
	  };
    }
  });
  // Re-render with the new array
  setShapes(nextShapes);
}

// replace item with map
function handleIncrementClick(index) {
const nextCounters = counters.map((c, i) => {
  if (i === index) {
	// Increment the clicked counter
	return c + 1;
  } else {
	// The rest haven't changed
	return c;
  }
});
setCounters(nextCounters);
}

// insert at location with spread and slice
function handleClick() {
const insertAt = 1; // Could be any index
const nextArtists = [
  // Items before the insertion point:
  ...artists.slice(0, insertAt),
  // New item:
  { id: nextId++, name: name },
  // Items after the insertion point:
  ...artists.slice(insertAt)
];
setArtists(nextArtists);
setName('');
}

// ultimate changes
function handleClick() {
  const nextList = [...list];
  nextList.reverse();
  setList(nextList);
}
// can't mutate existing items inside due to shallow copy
// Solution
setMyList(myList.map(artwork => {
  if (artwork.id === artworkId) {
    // Create a *new* object with changes
    return { ...artwork, seen: nextSeen };
  } else {
    // No changes
    return artwork;
  }
});
```

> **Spread syntax** (`...`) allows an iterable, such as an array or string, to be expanded in places where zero or more arguments (for function calls) or elements (for array literals) are expected. In an object literal, the spread syntax enumerates the properties of an object and adds the key-value pairs to the object being created.

The [`useState`](https://beta.reactjs.org/apis/react/useState) Hook provides those two things:

1. A **state variable** to retain the data between renders.
2. A **state setter function** to update the variable and trigger React to render the component again.

When using [[React Component]], it is updated with [[React Hooks]]
