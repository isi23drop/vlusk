from flask import Blueprint, jsonify, make_response
from flask.json import jsonify
from app.controllers.alumni_ctr import index, get_all_ctr, get_user_ctr, update_ctr, delete_ctr
from app.models.machine import Alumni

blueprint = Blueprint('alumni', __name__)


# (get_all_ctr)
@blueprint.route('/alumni/<name>', methods=['GET'])
def create_user(name):
    return make_response(jsonify('created user!'), 200)


@blueprint.route('/alumni', methods=['GET'])
def get_user():
    try:
        users = Alumni.query.all()
        return make_response(jsonify([user.json() for user in users]), 200)
    except Exception:
        return make_response(jsonify({'message': 'error getting users'}), 200)
# blueprint.route('/alumni/<int:id>', methods=['GET'])(get_user_ctr)
# blueprint.route('/alumni/<int:id>', methods=['PUT'])(update_ctr)
# blueprint.route('/alumni/<int:id>', methods=['DELETE'])(delete_ctr)
