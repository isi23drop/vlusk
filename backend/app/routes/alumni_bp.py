from flask import Blueprint
from app.controllers.alumni_ctr import index, get_all_ctr, get_user_ctr, update_ctr, delete_ctr
#from app.models.machine import Alumni

blueprint = Blueprint('alumni', __name__)

blueprint.route('/alumni', methods=['GET'])(get_all_ctr)
blueprint.route('/alumni/<int:id>', methods=['GET'])(get_user_ctr)
blueprint.route('/alumni/<int:id>', methods=['PUT'])(update_ctr)
blueprint.route('/alumni/<int:id>', methods=['DELETE'])(delete_ctr)
