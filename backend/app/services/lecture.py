from flask import Flask, request, jsonify, make_response
#from app.app import app, db
from app.models.machine import Lecture


# get all lectures
#@app.route('/lectures', methods=['GET'])
def get_all_lectures():
    try:
        lectures = Lecture.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify([lectures.json() for lectures in lectures]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting lectures'}), 500)

#
# get lecture by id
#
#@app.route('/lectures/<int:id>', methods=['GET'])
def get_lecture(id):
    try:
        lecture = Lecture.query.filter_by(id=id).first()
        if lecture:
            return make_response(jsonify({'lecture': lecture.json()}), 200)
        return make_response(jsonify({'message': 'lecture not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting lecture'}), 500)

# update Lecture
#@app.route('/lectures/<int:id>', methods=['PUT'])
def update_lecture(id):
    try:
        lecture = Lecture.query.filter_by(id=id).first()
        # check for existence of primary keys; defined in models.machine
        if lecture:
            data = request.get_json()
            lecture.username = data['username']
            lecture.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message': 'lecture updated'}), 200)
        return make_response(jsonify({'message': 'lecture not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error updating lecture'}), 50)

# delete Lecture
#@app.route('/lectures/<int:id>', methods=['DELETE'])
def delete_lecture(id):
    try:
        lecture = Lecture.query.filter_by(id=id).first()
        if lecture:
            db.session.delete(lecture)
            db.session.commit()
            return make_response(jsonify({'message': 'lecture deleted'}), 200)
        return make_response(jsonify({'message': 'lecture not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting lecture'}), 500)
