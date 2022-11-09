from flask import Blueprint, render_template
from flask_login import login_user, login_required, logout_user

views = Blueprint('views',__name__)

@views.route('/')
def home():
    return render_template("index.html")

@views.route('/')
def signup():
    return render_template("signup.html")

@views.route('/')
def features():
    return render_template("features.html")