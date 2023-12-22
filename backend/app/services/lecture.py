from flask import request, jsonify, make_response


# get all lectures
def get_all_lectures(Lecture):
    try:
        lectures = Lecture.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify(
            [lecture.json() for lecture in lectures]
            ), 200)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] getting lectures'}
            ), 500)


# get lecture by id
def get_lecture(Lecture, id):
    try:
        lecture = Lecture.query.filter_by(id=id).first()
        if lecture:
            return make_response(jsonify({'lecture': lecture.json()}), 200)
        return make_response(jsonify({'message': 'lecture not found'}), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] getting lecture'}
            ), 500)


# update Lecture
def update_lecture(Lecture, id):
    try:
        lecture = Lecture.query.filter_by(id=id).first()
        # check for existence of primary keys; defined in models.machine
        if lecture:
            data = request.get_json()
            lecture.id = data['id']
            lecture.codigo = data['codigo']
            Lecture.session.commit()
            return make_response(jsonify({'message': 'lecture updated'}), 200)
        return make_response(jsonify({'message': 'lecture not found'}), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] updating lecture'}
            ), 50)


# delete Lecture
def delete_lecture(Lecture, id):
    try:
        lecture = Lecture.query.filter_by(id=id).first()
        if lecture:
            Lecture.session.delete(lecture)
            Lecture.session.commit()
            return make_response(jsonify({'message': 'lecture deleted'}), 200)
        return make_response(jsonify({'message': 'lecture not found'}), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] deleting lecture'}
            ), 500)
