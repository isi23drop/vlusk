from flask import Flask, request, jsonify, make_response
from app.app import app, db
from models.machine import History


# create a User
@app.route('/history/create', methods=['GET'])
def get_users():
    try:
        users = History.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users'}), 500)

#
# get user by id
#
@app.route('/history<int:id>', methods=['GET'])
def get_user(id):
    try:
        userHist_id = History.query.filter_by(id=id).first()
        if userHist_id:
            return make_response(jsonify({'user': user.json()}), 200)
        return make_response(jsonify({'message': 'user id not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting user'}), 500)

# update User
@app.route('/history/<int:id>', methods=['PUT'])
def update_user(id):
    try:
        userHist_id = History.query.filter_by(id=id).first()
        if userHist_id:
            data = request.get_json()
            userHist_id.username = data['username']
            userHist_id.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'user history updated'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error updating user'}), 50)

# delete User
@app.route('/history/<int:id>', methods=['DELETE'])
def delete_user(id):
    try:
        user_history = History.query.filter_by(id=id).first()
        if user_history:
            db.session.delete(user_history)
            db.session.commit()
            return make_response(jsonify({'message': 'user history deleted'}), 200)
        return make_response(jsonify({'message': 'user history not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting user history'}), 500)
