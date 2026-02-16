from flask import Flask, render_template, redirect, url_for, flash
from forms import RegistrationForm
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = "super-secret-key"
csrf=CSRFProtect(app)

@app.route("/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data

        flash(f"Welcome {name}! Registration successful", "success")
        return redirect(url_for("success"))

    return render_template("register.html", form=form)


@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
