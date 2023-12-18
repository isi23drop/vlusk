from flask_sqlalchemy import create_engine
from flask_sqlalchemy.sql import text
import json
from app.models.machine import Alumni, Lecture, History, db
from os import environ


def create_logic():
    try:
        db.create_all()
        db.session.commit()
        return 'TABLES CREATED'
    except Exception as e:
        print(e)
        return 'TABLES NOT CREATED'

def insert_logic():
    #data =

    engine = create_engine(environ.get('DB_URL'))
    with engine.connect() as pgconn:
        #for file in
        file = open('./migrations/')


