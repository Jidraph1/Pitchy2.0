from . import db 

class User(db.Model):
    __tablename__= 'users'
    id=db.Column(db.Integer, primary_key = True)
    username = id.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'