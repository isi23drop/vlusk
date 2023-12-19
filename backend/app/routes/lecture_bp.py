from flask import Blueprint
from app.controllers.lecture_ctr import get_all_lec_ctr, get_lec_ctr, update_ctr, delete_ctr
from app.models.machine import Lecture

blueprint = Blueprint('lectures', __name__)

blueprint.route('/lectures', methods=['GET'])(get_all_lec_ctr)
blueprint.route('/lectures/<int:id>', methods=['GET'])(get_lec_ctr)
blueprint.route('/lectures/<int:id>', methods=['PUT'])(update_ctr)
blueprint.route('/lectures/<int:id>', methods=['DELETE'])(delete_ctr)
