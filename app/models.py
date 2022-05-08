from . import db

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String) 
    pitches = db.relationship('Pitch', backref='owner')
    comments = db.relationship('Comment', backref='owner')
    def __repr__(self):
        return f"User('{self.username}')"