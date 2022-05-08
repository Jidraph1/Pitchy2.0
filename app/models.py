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
    '''
    '''
    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(), index=True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)  
    def __repr__(self):
            return f'Pitch {self.description}'

 


