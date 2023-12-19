from flask import Flask
from os import environ
from flask_migrate import Migrate
# routes
from app.routes.alumni_bp import blueprint as alumni_bp
from app.routes.lecture_bp import blueprint as lecture_bp
from app.routes.history_bp import blueprint as history_bp

#
from .extensions import (
        db,
        login_manager,
        migrate
        )

def create_app(config_object="app.settings"): # ci env check base repo
    """ create application factory """
    app = Flask(__name__.split(".")[0])
    #app.config.from_object('config')
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)


    #app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

    # register blueprints
    #app.register_blueprint(blueprint, url_prefix='/machines')
    #app.register_blueprint(alumni_bp, url_prefix='/alumni')
    #app.register_blueprint(lecture_bp, url_prefix='/lectures')
    #app.register_blueprint(history_bp, url_prefix='/history')

    return app

def register_extensions(app):
    """ register flask extensions """
    db.init_app(app)
    #migrate.init_app(app, db)
    #login_manager.init_app(app)
    return None

def register_blueprints(app):
    """ register flask blueprints """
    app.register_blueprint(alumni_bp, url_prefix='/alumni')
    app.register_blueprint(lecture_bp, url_prefix='/lectures')
    app.register_blueprint(history_bp, url_prefix='/history')

    return None

# migration code
#migrate = Migrate(app, db)

if __name__ == '__main__':
    create_app()[0].run(host='127.0.0.1', port=5000, debug=True)

