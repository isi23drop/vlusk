from flask import jsonify
from app.models.machine import db, Alumni, Lecture, History
#from app.services.user_service import insert_logic, create_logic


def index(table):
    return jsonify({'status': 'OK',
                    'localhost:5000/machines/create': 'create table in postgres database',
                    'localhost:5000/machines/insert': f'insert table in postgres database{table}'})

#def create():
    #create_logic()

#def insert():
    #insert_logic()





