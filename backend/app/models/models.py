from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

class User(UserMixin, db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    surname = db.Column(db.String(1000))
    id = db.Column(db.Integer, primary_key=True)

    def set_password(self, password):
        # create password and hash it
        password = generate_password_hash(password, method='sha256')


    def check_password(self, password):
        # check hashed password
        return check_password_hash(self.password, password)


    def __repr__(self):
        return '<User {}>'.format(self.id)

