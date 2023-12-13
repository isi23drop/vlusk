from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from os import environ

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)

def json(self):
    return {'id': self.id,
            'username': self.username,
            'email': self.email
            }

db.create_all()

# create a test route
@app.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)

# create a User
@app.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify([user.json() for user in users]), 200)
    except e:
        return make_response(jsonify({'message': 'error getting users'}), 500)

#
# get user by id
#
@app.route('/users<int:id>', methods=['GET'])
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except e:
        return make_response(jsonify({'message': 'error getting user'}), 500)

# update User
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user updated'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except e:
        return make_response(jsonify({'message': 'error updating user'}), 50)

# delete User
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()
            return make_response(jsonify({'message': 'user deleted'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except e:
        return make_response(jsonify({'message': 'error deleting user'}), 500)
