from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user    
 

auth = Blueprint('auth',__name__)

@auth.route('/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if(check_password_hash(user.password, password)):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
            else:
                flash('Incorrect password, try again', category='failure')
        else:
            flash('Email does not exist', category='Failure')        
    return render_template ("login.html")

@auth.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    

@auth.route('/signup/',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm password')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exist',category='Failure')
        elif len(email) < 4:
            flash('Email must be longer', category='error')
        elif len(name) < 2:
            flash('Name should be longer', category='error')
        elif len(password) < 8:
            flash('password must be 8 characters', category='error')
        elif password != confirm_password:
            flash('Passowrd not matching with the previous', category='error')
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password,method='sha26'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, rememebr=True)
            flash('Account Created', category='success')
            return redirect(url_for('views.home'))
            # add user to the database

    return render_template("signup.html", boolean=True)

@auth.route('/features/')
def features():
    return render_template("features.html")
