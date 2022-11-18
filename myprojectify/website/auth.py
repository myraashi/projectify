from os import name
from xmlrpc.client import boolean
from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User,Note
from werkzeug.security import generate_password_hash,check_password_hash
from web1 import db
from flask_login import login_user,login_required,logout_user,current_user
#from flask.ext.uuid import FlaskUUID

auth=Blueprint('auth',__name__)

@auth.route('/features/',methods=['GET','POST'])
def features():
    return render_template('features.html',boolean=True)

@auth.route('/index/',methods=['GET','POST'])
def index():
    return render_template('index.html',boolean=True)

@auth.route('/home/<name>',methods=['GET','POST'])
@login_required
def home(name):

    if request.method=='POST':
        note=request.form.get('Note')

        if len(note) < 1:
            flash('Note too short!',category='error')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note successfully added!',category='success')

    return render_template('home.html',boolean=True)

@auth.route('/responsivecontact/',methods=['GET','POST'])
def contact():
    return render_template('responsivecontact.html',boolean=True)


@auth.route('/login/',methods=['GET','POST'])
def login():
    return render_template('login.html',boolean=True)

@auth.route('/logout/')
@login_required
def logout():
    #logout_user()
    return render_template('index.html',boolean=True)#redirect(url_for('views.home'))

@auth.route('/signin/',methods=['GET','POST'])
def signin():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')

        user=User.query.filter_by(email=email).first()
        print (user.email)
        if user:
            if check_password_hash(user.password,password):
                flash('Login successful',category='success')
                login_user(user,remember=True)
                return redirect(url_for('auth.home',name=user))
            else:
                flash('Incorrect password',category='error')
                render_template('login.html',boolean=True)
        else:
            flash('Email does not exist!',category='error')            
            return render_template('login.html',boolean=False)
    return render_template('home.html',boolean=True)

@auth.route('/signup/',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        
        user=User.query.filter_by(email=email).first()
        print(user)
        if user:
            flash('Email already exist!',category='error')
        elif len(email)<3:
            flash('email must be atleast 2 characters.',category='error') 
        elif len(name)<2:
            flash('first name must be atlest 1 charater.',category='error')
        elif password1!=password2:
            flash('password is not macthing.',category='error')
        elif len(password1)<7:
            flash('password must be atleast 7 characters.',category='error')
        else :
            new_user =User(name=name,email=email,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!',category='success')
            #login_user(user,remember=True)
            return redirect(url_for('auth.home',name=user))
        return render_template('login.html',boolean=False)

    return render_template("home.html") 
