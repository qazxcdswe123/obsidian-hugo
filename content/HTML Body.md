# `<body>`
- `<p>` = paragraph
- `<h1>...<h6>` = heading
- `<ul>` = unordered list / dot
- `<ol>` = ordered list / number
- `<table>`
	- `<thead>` = header in table
		- `<tr>` = tags as row (add a row)
			- `<td>` = tags for individual cells
- `<img alt="alternative text for accessibility" src="PATH">`
- `<video autoplay loop muted width="1280">`
	- `<source> src="PATH" type="video/mp4"`
	- `</video>`
- `<a>` = anchor, tag
	- `<a href="https://www.harvard.edu">Harvard</a>`
	- href = hypertext reference
- `<form>`
	```html
	<form action="https://www.google.com/search" method="get">
        <input name="q" type="text">
        <input type="submit">
    </form>
	```
	- First, we have a `<form>` tag that has an `action` of Google’s search URL, with a method of GET.
	- Inside the form, we have one `<input>`, with the name `q`, and another `<input>` with the type of `submit`. When the second input, a button, is clicked, the form will automatically add the input to the URL.
	- So when we open `search.html` in our browser, we can use the form to search via Google.