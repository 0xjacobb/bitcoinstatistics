import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User

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

if __name__ == '__main__':
    app.run()