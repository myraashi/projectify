#from crypt import methods
from flask import Blueprint,render_template,request,flash,json,jsonify
from flask_login import login_required,current_user
from web1 import db
from .models import Note
views=Blueprint('views',__name__)

@views.route('/',methods=['GET','POST'])
#@login_required
def home():
    if request.method=='POST':
        note=request.form.get('Note')

        if len(note) < 1:
            flash('Note too short!',category='error')
        else:
            new_note=Note(data=note,user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note successfully added!',category='success')

    return render_template("index.html",user=current_user)

# @views.route('/delete-note',methods=['POST'])
# def delete_note():
#     note=json.loads(request.data)
#     noteId=note['noteId']
#     note=Note.query.get(noteId)

    # if note:
    #     if Note.user_id == current_user.id:
    #        db.session.delete(note)
    #        db.session.commit()
           
    #     return jsonify({})
