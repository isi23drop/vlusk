from flask import Blueprint
from controllers.lecture_ctr import get_all_lec_ctr, get_lec_ctr, update_ctr, delete_ctr

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/lectures', methods=['GET'])(get_all_lec_ctr)
blueprint.route('/lectures/<int:id>', methods=['GET'])(get_lec_ctr)
blueprint.route('/lectures/<int:id>', methods=['PUT'])(update_ctr)
blueprint.route('/lectures/<int:id>', methods=['DELETE'])(delete_ctr)
