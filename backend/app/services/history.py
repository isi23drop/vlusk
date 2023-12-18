from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, make_response
#from app.app import app, db
from app.models.machine import History

db = SQLAlchemy()

# get all history
#@app.route('/history', methods=['GET'])
def get_all_hist():
    try:
        history = History.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify([item.json() for item in history]), 200)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting users'}), 500)

#
# get history by id (terms)
#
#@app.route('/history/<int:id>', methods=['GET'])
def get_term(id):
    # each user has a history. For the full history, each id are terms.
    try:
        history_term = History.query.filter_by(id=id).first()
        if history_term:
            return make_response(jsonify(
                {f'term {id} for the user history:': history_term.json()}
                ), 200)
        return make_response(jsonify(
            {'message': 'history term id not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': 'error getting history term id'}
            ), 500)

# update history
#@app.route('/history/<int:id>', methods=['PUT'])
def update_history(id):
    try:
        history_term = History.query.filter_by(id=id).first()
        if history_term:
            data = request.get_json()
            history_term.username = data['username']
            history_term.email = data['email']
            db.session.commit()
            return make_response(jsonify(
                {'message': 'history term by id updated'}
                ), 200)
        return make_response(jsonify(
            {'message': 'history term by id not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error updating history term'}), 50)

# delete history term
#@app.route('/history/<int:id>', methods=['DELETE'])
def delete_history(id):
    try:
        history_term = History.query.filter_by(id=id).first()
        # check for history primary keys
        if history_term:
            db.session.delete(history_term)
            db.session.commit()
            return make_response(jsonify({'message': 'history term deleted'}), 200)
        return make_response(jsonify({'message': 'history term not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting history term'}), 500)
