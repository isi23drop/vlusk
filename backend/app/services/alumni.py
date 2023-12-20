#from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify, make_response, current_app
#from app.models.machine import Alumni, db

#print(f'from services.alumni: {type(Alumni)}')
#print(f'from services.alumni: {type(db.query)}')

#print(f'from services.alumni: {type(current_app.name)}') print(f'from services.alumni: {type(current_app.name)}')
'''
from services.alumni: <class 'flask_sqlalchemy.model.DefaultMeta'>
from services.alumni: <class 'module'>
'''

'''
# create if does not exist
def create_app():
    with current_app: #app.app_context():
        db.create_all()
    return app
'''

#print('hmmmmmmm')
# get all alumni
def get_all_alumni_v2(Alumni):
    print("in services")
    try:
        alumni = Alumni(name=Alumni)
        print(f'from services.alumni: {type(alumni)}')
        #alumni = Alumni.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify([item.json() for item in alumni]), 200)
    except Exception as e:
        print(f'Error: {e}')
        return make_response(jsonify({'message': 'error getting alumni'}), 500)

def get_all_alumni(Alumni):
    try:
        users = Alumni.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception:
        return make_response(jsonify({'message': 'error getting users'}), 200)
#
# get alumni by id
def get_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            return make_response(jsonify({'alumni': alumni.json()}), 200)
        return make_response(jsonify({'message': 'alumni not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error getting alumni'}), 500)

# update alumni
def update_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            data = request.get_json()
            alumni.username = data['username']
            alumni.email = data['email']
            Alumni.session.commit()
            return make_response(jsonify({'message': 'user updated'}), 200)
        return make_response(jsonify({'message': 'user not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error updating user'}), 50)

# delete alumni
def delete_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            Alumni.session.delete(alumni)
            Alumni.session.commit()
            return make_response(jsonify({'message': 'alumni deleted'}), 200)
        return make_response(jsonify({'message': 'alumni not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message': 'error deleting alumni'}), 500)
