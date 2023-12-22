from flask import Blueprint
from app.controllers.history_ctr import get_all_hist_ctr, get_hist_term_ctr, update_ctr, delete_ctr, get_by_lecture_ctr

blueprint = Blueprint('history', __name__)

blueprint.route('/history/', methods=['GET'])(get_all_hist_ctr)
blueprint.route('/history/<int:id_alumni>/<int:id_lecture>/', methods=['GET'])(get_hist_term_ctr)

#broken
#blueprint.route('/history/<int:id_lecture>/<int:id_alumni>', methods=['GET'])(get_by_lecture_ctr)

#todo
blueprint.route('/history/<int:id>/', methods=['PUT'])(update_ctr)
blueprint.route('/history/<int:id>/', methods=['DELETE'])(delete_ctr)
