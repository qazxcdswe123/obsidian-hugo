---
aliases: []
date created: Oct 19th, 2022
date modified: Mar 17th, 2023
---

# Basic Css
Anything in CSS between `/*` and `*/` is a **CSS comment**  
Add between head include

```html
<link href="styles/style.css" rel="stylesheet">
```

CSS layout is mostly based on the _box model._ Each box taking up space on your page has properties like:

- `padding`, the space around the content. In the example below, it is the space around the paragraph text.
- `border`, the solid line that is just outside the padding.
- `margin`, the space around the outside of the border.

![three boxes sat inside one another. From outside to in they are labelled margin, border and padding](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics/box-model.png)

The [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body) is a **block** element, meaning it takes up space on the page. The margin applied to a block element will be respected by other elements on the page. In contrast, images are **inline** elements, for the auto margin trick to work on this image, we must give it block-level behavior using `display: block;`.

## Collections
`!important`: to override the original css