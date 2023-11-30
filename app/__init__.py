import os
from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from flask_session import Session
#from .config import dev_config, prod_config

#dbal = SQLAlchemy()
#session = Session()

def create_app(test_config=None):
    app = Flask(__name__,instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
            )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    def hello():
        return 'hello, world!'


    # init SQLAlchemy
    #dbal.init.app()

    # call sqlite3 database
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    #from .main import main as main_blueprint
    #app.register_blueprint(main_blueprint)

    #from .auth import auth as auth_blueprint
    #app.register_blueprint(auth_blueprint)

    return app
