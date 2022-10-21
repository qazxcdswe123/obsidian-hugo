## React Hooks
Functions starting with `use` are called _Hooks_. `useState` is a built-in Hook provided by React. You can find other built-in Hooks in the [React API reference.](https://beta.reactjs.org/apis/react) You can also write your own Hooks by combining the existing ones.

In React, `useState`, as well as any other function starting with ”`use`”, is called a Hook.  
_Hooks_ are special functions that are only available while React is [rendering](https://beta.reactjs.org/learn/render-and-commit#step-1-trigger-a-render) (which we’ll get into in more detail on the next page). They let you “hook into” different React features.

### Pitfall
**Hooks—functions starting with `use`—can only be called at the top level of your components or [your own Hooks.](https://beta.reactjs.org/learn/reusing-logic-with-custom-hooks)** You can’t call Hooks inside conditions, loops, or other nested functions. Hooks are functions, but it’s helpful to think of them as unconditional declarations about your component’s needs. You “use” React features at the top of your component similar to how you “import” modules at the top of your file.