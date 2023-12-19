from flask import jsonify
#from app.models.machine import Alumni
from app.services.alumni import get_all_alumni, get_alumni, update_alumni, delete_alumni

def index(table):
    return jsonify({'status': 'OK',
                    'localhost:5000/machines/create': 'create table in postgres database',
                    'localhost:5000/machines/insert': f'insert table in postgres database{table}'})


def get_all_ctr():
    get_all_alumni()


def get_user_ctr(Alumni, id):
    get_alumni(Alumni, id)


def update_ctr(Alumni, id):
    update_alumni(Alumni, id)


def delete_ctr(Alumni, id):
    delete_alumni(Alumni, id)




