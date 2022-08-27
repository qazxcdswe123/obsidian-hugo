---
aliases: []
tags: []
date created: Aug 25th, 2022
date modified: Aug 25th, 2022
---
# `<head>`
- `<title>` = text in tab
- `<link rel="stylesheet" href="main.css">`

## Viewport
[Responsive Web Design Viewport](https://www.w3schools.com/css/css_rwd_viewport.asp)
The viewport is the user's visible area of a web page.

The viewport varies with the device, and will be smaller on a mobile phone than on a computer screen.

Before tablets and mobile phones, web pages were designed only for computer screens, and it was common for web pages to have a static design and a fixed size.

Then, when we started surfing the internet using tablets and mobile phones, fixed size web pages were too large to fit the viewport. To fix this, browsers on those devices scaled down the entire web page to fit the screen.

This was not perfect!! But a quick fix

[Viewport meta tag - HTML: HyperText Markup Language | MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Viewport_meta_tag)

## Example

```html
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!--<meta http-equiv="X-UA-Compatible" content="ie=edge"> -->
<!--As this answer is now 10+ years old my recommendation would be to leave this tag out altogether, unless you must support old legacy browsers.-->
<title>Sha3-256 File Hash Online</title>
<link rel="stylesheet" href="main.css">
```