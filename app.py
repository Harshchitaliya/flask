from flask import Flask, render_template, request, redirect,session
from db import Database
import api

app: Flask = Flask(__name__)

dbo = Database()


@app.route("/")
def index():
    return render_template("login.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/perform_registration", methods=["post"])
def perform_registration():
    Name = request.form.get("username")
    Email = request.form.get("email")
    Password = request.form.get("password")
    response = dbo.insert(Name, Email, Password)
    if response == 1:
        return render_template("login.html", message="registration successful, Log in here")
    else:
        return render_template("register.html", message="Email already exists")


@app.route("/perform_login", methods=["post"])
def perform_login():
    email = request.form.get("email")
    password = request.form.get("password")

    response = dbo.search(email, password)

    if response == 1:
        session["login"]=1
        return redirect("/profile")
    else:
        return render_template("login.html", message="incorrect Email/Password")


@app.route("/profile")
def profile():
    if session:
        return render_template("profile.html")
    else:
        return redirect("/")


@app.route("/Ner")
def ner():
    if session:
        return render_template("ner.html")
    else:
        return redirect("/")

@app.route("/perform_ner",methods=["post"])
def perform_ner():
    if session:
        text = request.form.get("text")
        response = api.ner(text)
        print(response)

        return render_template("ner.html" , response = response)
    else:
        return redirect("/")



# @app.route("/sentiment_analysis")
# def sentiment_analysis():
#     return "sentiment_analysis"
#
#
# @app.route("/abuse_detection")
# def abuse_detection():
#     return "abuse_detection"
app.run(debug=True)
