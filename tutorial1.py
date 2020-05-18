from flask import Flask, redirect, url_for, render_template

app=Flask(__name__)

myname='ritish'

@app.route("/")
def home():
    return "Hello! This is the MAIN PAGE <h1>HELLO</h1>"

@app.route("/<name>")
def user(name):
    return f"My name is {name}"


@app.route("/admin")
def admin():
    if myname=='ritish':
        return redirect(location=url_for(endpoint="user", name=myname))
    else:
        return redirect(location=url_for(endpoint="home"))

if __name__=="__main__":
    app.run()
