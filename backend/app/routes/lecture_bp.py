from flask import Blueprint
from app.controllers.lecture_ctr import (
        get_all_lec_ctr, get_lec_ctr,
        update_lec_ctr, delete_lec_ctr
        )

blueprint = Blueprint('lectures', __name__)


@blueprint.route('/lectures/', methods=['GET'])
def get_all_lec_routes():
    return get_all_lec_ctr()


@blueprint.route('/lectures/<int:id>', methods=['GET'])
def get_lec_routes(id):
    return get_lec_ctr(id=id)


@blueprint.route('/lectures/<int:id>', methods=['PUT'])
def update_lec_routes(id):
    return update_lec_ctr(id=id)


@blueprint.route('/lectures/<int:id>', methods=['DELETE'])
def delete_lec_routes(id):
    return delete_lec_ctr(id=id)
