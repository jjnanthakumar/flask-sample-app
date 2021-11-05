from flask import Blueprint

from flask import jsonify, request, render_template, redirect, url_for
import pandas as pd

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html",name = "Nanthakumar J J")

@views.route("/profile/<user>")
def profile(user):
    return render_template("index.html",name = user)

@views.route("/employees/json")
def getJson():
    df = pd.read_csv('employees.csv')
    return jsonify(df.to_dict())

@views.route("/redirect")
def gotopage():
    return redirect(url_for("views.getJson"))
