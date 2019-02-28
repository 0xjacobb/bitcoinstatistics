from flask import request, jsonify, render_template, url_for, redirect
from bitcoinstatistics.models import User
from bitcoinstatistics import app
from bitcoinstatistics import db

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/add")
def add_user():
    firstName=request.args.get('firstName')
    secondName=request.args.get('secondName')
    eMail=request.args.get('eMail')
    try:
        user=User(
            firstName=firstName,
            secondName=secondName,
            eMail=eMail
        )
        db.session.add(user)
        db.session.commit()
        return "User added. user id={}".format(user.id)
    except Exception as e:
	    return(str(e))

@app.route("/add/form",methods=['GET', 'POST'])
def add_user_form():
    if request.method == 'POST':
        firstName=request.form.get('firstName')
        secondName=request.form.get('secondName')
        eMail=request.form.get('eMail')

        print(firstName, secondName, eMail, end='\n')
        try:
            user=User(
                firstName=firstName,
                secondName=secondName,
                eMail=eMail
            )
            db.session.add(user)
            db.session.commit()
            return "User added. user id={}".format(user.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")


@app.route("/getall")
def get_all():
    try:
        user=User.query.all()
        return  jsonify([e.serialize() for e in user])
    except Exception as e:
	    return(str(e))
