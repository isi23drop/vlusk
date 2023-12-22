from flask import Flask

# routes
from app.routes.alumni_bp import blueprint as alumni_bp
from app.routes.lecture_bp import blueprint as lecture_bp
from app.routes.history_bp import blueprint as history_bp

# extensions
from .extensions import db


# ci env check base repo
def create_app(config_object="app.settings"):
    """ create application factory """
    app = Flask(__name__.split(".")[0])
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)

    # print(f'from app.py: {app.app_context()}')
    # print(f'from app.py: {type(current_app.name)}')
    return app


def register_extensions(app):
    """ register flask extensions """
    db.init_app(app)

    return None


def register_blueprints(app):
    """ register flask blueprints """
    app.register_blueprint(alumni_bp)
    app.register_blueprint(lecture_bp)
    app.register_blueprint(history_bp)

    return None


if __name__ == '__main__':
    create_app()[0].run(host='127.0.0.1', port=5000, debug=True)
