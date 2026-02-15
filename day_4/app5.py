from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def home_page():
    return render_template("home5.html")


@app.route("/about5")
def about_page():
    return render_template("about5.html")