---
aliases: []
date created: Aug 25th, 2022
date modified: Aug 25th, 2022
---
# CSS Selectors
[CSS Selectors Reference](https://www.w3schools.com/cssref/css_selectors.asp)  
[MDN Ref](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors)

Used in [querySelector](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)

## What is a Selector
A CSS selector is the first part of a CSS Rule. It is a pattern of elements and other terms that tell the browser which HTML elements should be selected to have the CSS property values inside the rule applied to them. The element or elements which are selected by the selector are referred to as the _subject of the selector_.

Here are some of the more common types of selectors:
### Element Selector
`p`

### ID Selector
`#my-id`

### Class Selector
`.my-class`

### Attribute Selector
`img[src]`

### [Pseudo-class Selector](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Selectors#pseudo-classes_and_pseudo-elements)
`a:hover`



## Example
### :first-child Selector

```html
<!DOCTYPE html>

<html lang="en">
    <head>
        <style>
  
            p:first-child
            {
                font-size: larger;
            }
  
        </style>
        <title>paragraphs</title>
    </head>
    <body>
        <p>
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus convallis scelerisque quam, vel hendrerit lectus viverra eu. Praesent posuere eget lectus ut faucibus. Etiam eu velit laoreet, gravida lorem in, viverra est. Cras ut purus neque. In porttitor non lorem id lobortis. Mauris gravida metus libero, quis maximus dui porta at. Donec lacinia felis consectetur venenatis scelerisque. Nulla eu nisl sollicitudin, varius velit sit amet, vehicula erat. Curabitur sollicitudin felis sit amet orci mattis, a tempus nulla pulvinar. Aliquam erat volutpat.
        </p>
        <p>
            Mauris ut dui in eros semper hendrerit. Morbi vel elit mi. Sed sit amet ex non quam dignissim dignissim et vel arcu. Pellentesque eget elementum orci. Morbi ac cursus ex. Pellentesque quis turpis blandit orci dapibus semper sed non nunc. Nulla et dolor nec lacus finibus volutpat. Sed non lorem diam. Donec feugiat interdum interdum. Vivamus et justo in enim blandit fermentum vel at elit. Phasellus eu ante vitae ligula varius aliquet. Etiam id posuere nibh.
        </p>
        <p>
            Aenean venenatis convallis ante a rhoncus. Nullam in metus vel diam vehicula tincidunt. Donec lacinia metus sem, sit amet egestas elit blandit sit amet. Nunc egestas sem quis nisl mattis semper. Pellentesque ut magna congue lorem eleifend sodales. Donec tortor tortor, aliquam vitae mollis sed, interdum ut lectus. Mauris non purus quis ipsum lacinia tincidunt.
        </p>
    </body>
</html>
```

### Multiple Attribute
`document.querySelector('[name="single-5"][value="B"]')`
