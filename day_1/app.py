from flask import Flask, request

app=Flask(__name__)

@app.route("/")  #@ ka mtlb hota hai ki jab bhi koi user "/" path par aayega to yeh function chalega
def home():
    return "Hello, World! this is my first flask app"  # yeh function "Hello, World!" return karega jab user "/" path par aayega

@app.route("/about")  # jab bhi koi user "/about" path par aayega to yeh function chalega
def about():
    return "This is the about page of my first flask app"  # yeh function "This is the about page of my first flask app" return karega jab user "/about" path par aayega

@app.route("/contact")
def contact():
    return "this is my contact page of my first flask app"

@app.route("/submit",methods =["POST","GET"])
def submit():
    if request.method=="POST":
        return "You have submitted the form"
    else:
        return "This is the form page and u are only viewing it "