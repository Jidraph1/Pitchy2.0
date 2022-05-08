from . import db 

class User(db.Model):
    __tablename__= 'user'
    id=db.Column(db.Integer, primary_key = True)
    username = id.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    pitches = db.relationship(db.String)
    

    def __repr__(self):
        return f'User {self.username}'