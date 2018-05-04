from flask import Flask, render_template, redirect, request, flash, session
import re

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    fname = request.form["fname"]
    lname = request.form["lname"]
    email = request.form["email"]
    password = request.form["password"]
    cpassword = request.form["cpassword"]
    
    # check for empty fields
    count = is_blank(fname,lname,email,password,cpassword)    
    if count > 0:
        return redirect("/")
    # check first and last names contain only letters
    if not fname.isalpha():
        flash("first name cannot contain numbers")
        return redirect("/")
    if not lname.isalpha():
        flash("last name cannot contain numbers")
        return redirect("/")
    # check password length at least 8 characters long
    if len(password) < 8:
        flash("password has to be at least 8 characters long")
        return redirect("/")
    # email validation
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if len(email) < 1:
        flash("Email cannot be blank!")
        return redirect("/")
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email Address!")
        return redirect("/")
    # password match
    if password != cpassword:
        flash("password must match")
        return redirect("/")
    return render_template("success.html")

def is_blank(fname,lname,email,cpassword,password):
    count = 0
    if len(fname) < 1:
        flash("first name is required")
        count +=1
    if len(lname) < 1:
        flash("last name is required")
        count +=1
    if len(email) < 1:
        flash("email is required")
        count +=1
    if len(password) < 1:
        flash("password is required")
        count +=1
    if len(cpassword) < 1:
        flash("confirm password is required")
        count +=1
    return count

if __name__ == "__main__":
    app.run(debug=True)