from bitcoinstatistics import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String())
    secondName = db.Column(db.String())
    eMail = db.Column(db.String())

    def __init__(self, firstName, secondName, eMail):
        self.firstName = firstName
        self.secondName = secondName
        self.eMail = eMail 

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
    def serialize(self):
        return {
            'id': self.id, 
            'firstName': self.firstName,
            'secondName': self.secondName,
            'eMail ':self.eMail 
        }