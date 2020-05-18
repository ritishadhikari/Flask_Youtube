from flask import Flask, render_template, redirect, url_for

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index_t3.html")

@app.route("/test")
def test():
    return render_template(template_name_or_list="test_t3.html")


if __name__=="__main__":
    app.run()
