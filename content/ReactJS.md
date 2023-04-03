---
aliases: []
date created: Aug 22nd, 2022
date modified: Oct 18th, 2022
---
- [[React Component]]
- [[React Hooks]]
- [[React State]]

___

## Thinking in React
Original: [Thinking in React](https://beta.reactjs.org/learn/thinking-in-react)

### Step 1: Break the UI into a Component Hierarchy
Depending on your background, you can think about splitting up a design into components in different ways:
- **Programming**—use the same techniques for deciding if you should create a new function or object. One such technique is the [single responsibility principle](https://en.wikipedia.org/wiki/Single_responsibility_principle), that is, a component should ideally only do one thing. If it ends up growing, it should be decomposed into smaller subcomponents.
- **CSS**—consider what you would make class selectors for. (However, components are a bit less granular.)
- **Design**—consider how you would organize the design’s layers.  

Now that you’ve identified the components in the mockup, arrange them into a hierarchy. Components that appear within another component in the mockup should appear as a child in the hierarchy:
- `FilterableProductTable`
    - `SearchBar`
    - `ProductTable`
        - `ProductCategoryRow`
        - `ProductRow`

### Step 2: Build a Static Version in React
To build a static version of your app that renders your data model, you’ll want to build [components](https://beta.reactjs.org/learn/your-first-component) that reuse other components and pass data using [props.](https://beta.reactjs.org/learn/passing-props-to-a-component) Props are a way of passing data from parent to child. (If you’re familiar with the concept of [state](https://beta.reactjs.org/learn/state-a-components-memory), don’t use state at all to build this static version. State is reserved only for interactivity, that is, data that changes over time. Since this is a static version of the app, you don’t need it.)

### Step 3: Find the Minimal but Complete Representation of UI State
- Does it **remain unchanged** over time? If so, it isn’t state.
- Is it **passed in from a parent** via props? If so, it isn’t state.
- **Can you compute it** based on existing state or props in your component? If so, it _definitely_ isn’t state!

### Step 4: Identify Where Your State Should Live
For each piece of state in your application:

1. Identify _every_ component that renders something based on that state.
2. Find their closest common parent component—a component above them all in the hierarchy.
3. Decide where the state should live:
    1. Often, you can put the state directly into their common parent.
    2. You can also put the state into some component above their common parent.
    3. If you can’t find a component where it makes sense to own the state, create a new component solely for holding the state and add it somewhere in the hierarchy above the common parent component.

### Step 5: Add inverse data flow
