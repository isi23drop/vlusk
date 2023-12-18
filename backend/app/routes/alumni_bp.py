from flask import Blueprint
from controllers.alumni_ctr import index, get_all_ctr, get_user_ctr, update_ctr, delete_ctr

blueprint = Blueprint('blueprint', __name__)

blueprint.route('/alumni', methods=['GET'])(get_all_ctr)
blueprint.route('/alumni/<int:id>', methods=['GET'])(get_user_ctr)
blueprint.route('/alumni/<int:id>', methods=['PUT'])(update_ctr)
blueprint.route('/alumni/<int:id>', methods=['DELETE'])(delete_ctr)
