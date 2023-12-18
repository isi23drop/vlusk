from flask import Flask
from os import environ
from flask_migrate import Migrate
# routes
from app.routes.alumni_bp import blueprint as alumni_bp
from app.routes.lecture_bp import blueprint as lecture_bp
from app.routes.history_bp import blueprint as history_bp

# db
from app.models.machine import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    # init database
    db.init_app(app)

    # register blueprints
    #app.register_blueprint(blueprint, url_prefix='/machines')
    app.register_blueprint(alumni_bp, url_prefix='/alumni')
    app.register_blueprint(lecture_bp, url_prefix='/lectures')
    app.register_blueprint(history_bp, url_prefix='/history')

    return app

# migration code
migrate = Migrate(app, db)

if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=5000, debug=True)

