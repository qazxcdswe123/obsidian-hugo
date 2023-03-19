---
aliases: []
tags: []
date created: Oct 18th, 2022
date modified: Mar 15th, 2023
---

# React Hooks
Functions starting with `use` are called _Hooks_. `useState` is a built-in Hook provided by React. You can find other built-in Hooks in the [React API reference.](https://beta.reactjs.org/apis/react) You can also write your own Hooks by combining the existing ones.

In React, `useState`, as well as any other function starting with ”`use`”, is called a Hook.  
_Hooks_ are special functions that are only available while React is [rendering](https://beta.reactjs.org/learn/render-and-commit#step-1-trigger-a-render) . They let you “hook into” different React features.

## Pitfall
**Hooks—functions starting with `use`—can only be called at the top level of your components or [your own Hooks.](https://beta.reactjs.org/learn/reusing-logic-with-custom-hooks)** You can’t call Hooks inside conditions, loops, or other nested functions. Hooks are functions, but it’s helpful to think of them as unconditional declarations about your component’s needs. You “use” React features at the top of your component similar to how you “import” modules at the top of your file.

## `useCallback`
- [useCallback • React](https://beta.reactjs.org/reference/react/useCallback)

## `useEffect`
- Some components need to synchronize with external systems. For example, you might want to control a non-React component based on the React state, set up a server connection, or send an analytics log when a component appears on the screen. _Effects_ let you run some code after rendering so that you can synchronize your component with some system outside of React.
- [https://beta.reactjs.org/reference/react/useEffect](https://beta.reactjs.org/reference/react/useEffect)
