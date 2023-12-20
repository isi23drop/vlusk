from flask import jsonify
from app.models.machine import Lecture
from app.services.lecture import get_all_lectures, get_lecture, update_lecture, delete_lecture

def index(table):
    return jsonify({'status': 'OK',
                    'localhost:5000/machines/create': 'create table in postgres database',
                    'localhost:5000/machines/insert': f'insert table in postgres database{table}'})


def get_all_lec_ctr():
    get_all_lectures()


def get_lec_ctr(id):
    get_lecture()


def update_ctr(id):
    update_lecture(id)


def delete_ctr(id):
    delete_lecture(id)




