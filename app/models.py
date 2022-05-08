from . import db

class Users(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)
    password = db.Column(db.String) 
    #Relationship
    pitches = db.relationship('Pitch', backref='owner')
    comments = db.relationship('Comment', backref='owner')
    def __repr__(self):
        return f"User('{self.username}')"

class Pitch(db.Model):
    '''
    '''
    __tablename__ = 'pitches'
#one to many classes relationship
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    description = db.Column(db.String(), index=True)
    title = db.Column(db.String())
    category = db.Column(db.String(255), nullable=False)  
    def __repr__(self):
            return f'Pitch {self.description}' 

class Comment(db.Model):
    '''
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(255), index=True)
   
 
    def __repr__(self):
            return f'Comment {self.content}'   

class Comment(db.Model):
    '''
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(255), index=True)
   
 
    def __repr__(self):
            return f'Comment {self.content}'          
    