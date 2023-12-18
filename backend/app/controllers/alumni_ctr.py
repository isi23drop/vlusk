from flask import jsonify
from app.models.machine import db, Alumni, Lecture, History
from app.services.alumni import get_all_alumni, get_alumni, update_alumni, delete_alumni

def index(table):
    return jsonify({'status': 'OK',
                    'localhost:5000/machines/create': 'create table in postgres database',
                    'localhost:5000/machines/insert': f'insert table in postgres database{table}'})


def get_all_ctr():
    get_all_alumni()


def get_user_ctr(id):
    get_alumni()


def update_ctr(id):
    update_alumni(id)


def delete_ctr(id):
    delete_alumni(id)




