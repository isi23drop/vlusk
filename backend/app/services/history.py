from flask import request, jsonify, make_response


# get all history
def get_all_hist(History):
    try:
        history = History.query.all()
        # returns a jsonified function inside a list comprehension lambda lingo
        return make_response(jsonify([item.json() for item in history]), 200)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] getting users'}
            ), 500)


# experimental
def get_by_lecture(History, id_lecture, id_alumni):
    try:
        history_term = History.query.filter(
                (id_lecture == History.id_disciplina)
                (id_alumni == History.id_aluno)
                ).first()
        if history_term:
            return make_response(jsonify(
                {'term for the user history:': history_term.json()}
                ), 200)
        return make_response(jsonify(
            {'message': 'history term id not found'}
            ), 400)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] getting history term id.'}
            ))


#
# get history by id (terms)
def get_term(History, id_alumni, id_lecture):
    # each user has a history. For the full history, each id are terms.
    try:
        history_term = History.query.filter(
                (id_alumni == History.id_aluno),
                (id_lecture == History.id_disciplina)
                ).first()
        if history_term:
            return make_response(jsonify(
                {'term for the user history': history_term.json()}
                ), 200)
        return make_response(jsonify(
            {'message': 'history term id not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] getting history term id.'}
            ), 500)


# update history
def update_history(History, id_aluno):
    try:
        history_term = History.query.filter_by(id_aluno=id_aluno).first()
        if history_term:
            data = request.get_json()
            history_term.id_aluno = data['id_aluno']
            history_term.id_disciplina = data['id_disciplina']
            History.session.commit()
            return make_response(jsonify(
                {'message': 'history term by id updated'}
                ), 200)
        return make_response(jsonify(
            {'message': 'history term by id not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] updating history term'}
            ), 50)


# delete history term
def delete_history(History, id_aluno):
    try:
        history_term = History.query.filter_by(id_aluno=id_aluno).first()
        # check for history primary keys
        if history_term:
            History.session.delete(history_term)
            History.session.commit()
            return make_response(jsonify(
                {'message': 'history term deleted'}
                ), 200)
        return make_response(jsonify(
            {'message': 'history term not found'}
            ), 404)
    except Exception as e:
        return make_response(jsonify(
            {'message': f'error [{e}] deleting history term'}
            ), 500)
