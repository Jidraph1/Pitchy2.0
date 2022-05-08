from . import db 

class User(db.Model):
    __tablename__= 'user'
    id = db.Column(db.Integer, primary_key = True)
    username = id.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    pitches = db.relationship('Pitch', backref='owner')
    comment = db.relationship('Comment', backref='owner')
    
    def __repr__(self):
        return f'User {self.username}'

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = cd.Column(db.Integer, primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    description = db.Column(db.String())
    

