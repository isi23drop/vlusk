from flask import Blueprint
from app.controllers.history_ctr import get_all_hist_ctr, get_hist_term_ctr, update_ctr, delete_ctr

blueprint = Blueprint('history', __name__)

blueprint.route('/history', methods=['GET'])(get_all_hist_ctr)
blueprint.route('/history/<int:id>', methods=['GET'])(get_hist_term_ctr)
blueprint.route('/history/<int:id>', methods=['PUT'])(update_ctr)
blueprint.route('/history/<int:id>', methods=['DELETE'])(delete_ctr)
