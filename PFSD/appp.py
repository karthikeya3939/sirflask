from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def sam():
    return "Hello World"

@app.route("/<name>")
def sam1(name):
    return f'hi ... nee peru {name} inka nuvv erripuku vi'

@app.route("/template")
def sam2():
    return render_template("index.html")

@app.route("/india")
def sam22():
    return render_template("india.html")

@app.route("/KLU")
def sam221():
    return render_template("klu.html")

@app.route("/register")
def sam222():
    return render_template("register.html")


@app.route("/login")
def sam223():
    return render_template("login.html")

if __name__=="__main__":
    app.run()