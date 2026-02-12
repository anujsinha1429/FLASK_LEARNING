from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home ():
    return render_template("login.html")

@app.route("/submit",methods=["post"])
def login():
    username=request.form["username"] #iss line me form se username le rhe hai 
    password=request.form["password"] #iss line me form se password le rhe hai
    # if username=="oggy" and password=="123":
    #     return render_template("welcome.html",name=username)
    
# for so many users we can use dictionary


    valid_users={'oggy':'123','tom':'456','jerry':'789'}

    if username in valid_users and valid_users[username]==password:
        return render_template("lelcome.html",name=username)
    else:
        return "Invalid credentials. Please try again."