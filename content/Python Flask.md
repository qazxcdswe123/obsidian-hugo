[CS50](https://cs50.harvard.edu/college/2022/spring/notes/9/)
The `@` symbol in Python is called a **decorator**, which modifies a function.
[[Flask Template]]
# Composition
-   `app.py` will have the Python code for our web server.
-   `requirements.py` includes a list of required libraries for our application.
-   `static/` is a directory of static files, like images and CSS and JavaScript files.
	- `index.html`
	- `layout.html`
-   `templates/` is a directory for HTML files that will form our pages.

## layout.html
With the `{% %}` syntax, we can include placeholder blocks, or other chunks of code. Here we’ve named our block `body` since it contains the HTML that should go in the `<body>` element.
Basically placeholder 
# Lib
## request
`request.args.get("name")` catch `?name=David`
## render_template
`return render_template("index.html", name=name)`

`return render_template("greet.html", name=request.form.get("name", "world"))`
## redirect
use to redirect to another route
# Paradigm
![](https://s2.loli.net/2022/04/05/Ttbm2ndFkiau7Og.png)

-   The controller contains our “business logic”, code that manages our application overall, given user input. In Flask, this will be our Python code in `app.py`.
-   The view includes templates and visuals for the user interface, like the HTML and CSS that the user will see and interact with.
-   The model is our application’s data, such as a SQL database or CSV file, which we haven’t yet used.