from flask import Flask, render_template, redirect, url_for

app=Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template(template_name_or_list="index_t2.html", content=name, list_item=range(1,10))

if __name__=='__main__':
    app.run()
