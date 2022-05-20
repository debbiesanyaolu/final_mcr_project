from flask import render_template, redirect, url_for, Blueprint, request
my_view = Blueprint('my_view', __name__)

# app.config["SECRET_KEY"] = "SHHSECRETKEY"

@my_view.route("/")
def home():
    return render_template("home.html")

@my_view.route("/aboutmcr")
def aboutmcr():
    return render_template("aboutmcr.html")

@my_view.route("/aboutmanchester")
def aboutmanchester():
    return render_template("aboutmcr.html")

@my_view.route("/aboutliv")
def aboutliv():
    return render_template("aboutliv.html")

@my_view.route("/aboutliverpool")
def aboutliverpool():
    return render_template("aboutliv.html")

@my_view.route("/aboutbirm")
def aboutbirm():
    return render_template("aboutbirm.html")

@my_view.route("/aboutbirmingham")
def aboutbirmingham():
    return render_template("aboutbirm.html")

@my_view.route("/aboutldn")
def aboutldn():
    return render_template("aboutldn.html")

@my_view.route("/aboutlondon")
def aboutlondon():
    return render_template("aboutldn.html")

@my_view.route("/home")
def home_redirect():
    return redirect(url_for("my_view.home"))

@my_view.route("/homepage")
def homeb_redirect():
    return redirect(url_for("my_view.home"))