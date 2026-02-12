# day 2

from flask import Flask, request,Response,url_for,redirect,session

app=Flask(__name__)
app.secret_key="this"
# home page or login page 
@app.route ("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        user=request.form["username"]
        password=request.form["password"]
        if user=="admin" and password =="123":
            session["user"]=user # setting session variable
            return redirect(url_for("welcome"))
        else:
            return Response("invalid credentials. please try again",mimetype="text/plain") # returning plain text response
    return '''
    <h1 style="font-size: 30px;">Login Page</h1>
    <form method="post">
    username: <input type="text" name="username"><br>
    password: <input type="password" name="password"><br>
    <input type="submit" value="Login">
    </form>
    '''
# welcome page
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''Welcome {session['user']}! You have successfully logged in.
        <a href="{url_for("logout")}";">Logout</a>'''
        
    else:
        return redirect(url_for("login"))

    # logout page
@app.route("/logout")
def logout():
    session.pop("user",None) # removing session variable
    return redirect(url_for("login"))

        

