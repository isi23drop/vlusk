from flask import request, jsonify, make_response


# get all alumni
def get_all_alumni(Alumni):
    try:
        users = Alumni.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error {e} getting users'}
            ), 200)


# get alumni by id
def get_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            return make_response(jsonify(
                {'alumni': alumni.json()}
                ), 200)
        return make_response(jsonify(
            {'message': 'alumni not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error {e} getting alumni'}
            ), 500)


# update alumni
def update_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            data = request.get_json()
            alumni.id = data['id']
            alumni.cpf = data['cpf']
            Alumni.session.commit()
            return make_response(jsonify(
                {'message': 'user updated'}
                ), 200)
        return make_response(jsonify(
            {'message': 'user not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error {e} updating user'}
            ), 50)


# delete alumni
def delete_alumni(Alumni, id):
    try:
        alumni = Alumni.query.filter_by(id=id).first()
        if alumni:
            Alumni.session.delete(alumni)
            Alumni.session.commit()
            return make_response(jsonify(
                {'message': 'alumni deleted'}
                ), 200)
        return make_response(jsonify(
            {'message': 'alumni not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error {e} deleting alumni'}
            ), 500)
