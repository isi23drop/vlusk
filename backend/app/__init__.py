from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
#from app.extensions import db
from app.app import db as app_db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

    # init flask extensions
    #db = SQLAlchemy(app)
    #db.init_app(app)
    # init app_db
    app_db.init_app(app)

    # register blueprints
    #from app.main import bp as main_bp
    #app.register_blueprint(main_bp)

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'



    return app

