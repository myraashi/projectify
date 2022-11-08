from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login/', methods=['GET','POST'])
def login():
    return "<p>Login</p>"

@auth.route('/logout/')
def logout():
    return "<p>Logout</p>"

@auth.route('/signup/',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm password')
        
        if len(email) < 4:
            flash('Email must be longer', category='error')
        elif len(name) < 2:
            flash('Name should be longer', category='error')
        elif len(password) < 8:
            flash('password must be 8 characters', category='error')
        elif password != confirm_password:
            flash('Passowrd not matching with the previous', category='error')
        else:
            flash('Account Created', category='success')
            # add user to the database

    return render_template("signup.html")

@auth.route('/features/')
def features():
    return render_template("features.html")
