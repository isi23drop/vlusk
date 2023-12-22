from flask import Blueprint, jsonify, make_response
from app.controllers.alumni_ctr import (
        get_all_alumni_ctr, get_alumni_ctr,
        update_alumni_ctr, delete_alumni_ctr
        )

blueprint = Blueprint('alumni', __name__)


# test route
@blueprint.route('/alumni/<name>', methods=['GET'])
def test_alumni_route():
    return make_response(jsonify('created user!'), 200)


@blueprint.route('/alumni', methods=['GET'])
def get_all_route():
    return get_all_alumni_ctr()


@blueprint.route('/alumni/<int:id>', methods=['GET'])
def get_alumni_route(id):
    return get_alumni_ctr(id=id)


@blueprint.route('/alumni/<int:id>', methods=['PUT'])
def update_alumni_route(id):
    return update_alumni_ctr(id=id)


@blueprint.route('/alumni/<int:id>', methods=['DELETE'])
def delete_alumni_route(id):
    return delete_alumni_ctr(id=id)
