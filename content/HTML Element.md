-   Things in the head tag are things that shouldn't be rendered: information about the page and how to process it.
-   Things in the body tag are the things that should be displayed: the actual content.
-   JavaScript in the body is executed as it is read and as the page is rendered.
-   JavaScript in the head is interpreted before anything is rendered.
src: [MDN HTML basics](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/HTML_basics)
[[HTML Tag]]
![](https://s2.loli.net/2022/03/08/M4SBDkecYmJswnb.png)

![](https://s2.loli.net/2022/04/03/dxJfZLWeFnKmbBo.png)
`class` is the attribute _name_ and `editor-note` is the attribute _value_.

bold = `<p>My cat is <strong>very</strong> grumpy.</p>` 

image = `<img src="images/firefox-icon.png" alt="My test image">
`
-   `<head></head>` — the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head) element. This element acts as a **container for all the stuff you want to include on the HTML page that _isn't_ the content you are showing to your page's viewers.** This includes things like [keywords](https://developer.mozilla.org/en-US/docs/Glossary/Keyword) and a page description that you want to appear in search results, CSS to style our content, character set declarations, and more.
-   `<meta charset="utf-8">` — This element sets the character set your document should use to UTF-8 which includes most characters from the vast majority of written languages. Essentially, it can now handle any textual content you might put on it. There is no reason not to set this and it can help avoid some problems later on.
- Anything in HTML between `<!--` and `-->` is an **HTML comment**.