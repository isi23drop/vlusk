from flask import jsonify
#from app.models.machine import db, Alumni, Lecture, History
from app.services.history import get_all_hist, get_term, update_history, delete_history

def index(table):
    return jsonify({'status': 'OK',
                    'localhost:5000/machines/create': 'create table in postgres database',
                    'localhost:5000/machines/insert': f'insert table in postgres database{table}'})


def get_all_hist_ctr():
    get_all_hist()


def get_hist_term_ctr(id):
    get_term()


def update_ctr(id):
    update_history(id)


def delete_ctr(id):
    delete_history(id)
