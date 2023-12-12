import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    ROOT_PATH = basedir
    # below an example of a secret key. For the proof of concept,
    # this is used, but the best practice is to set environment
    # variables or secrets to handle these infos.
    SECRET_KEY = 'gV7S6iGV560ZikWik170'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"


class prod_config(Config):
    DEBUG = False
    TESTING = False
    #LOGIN_DISABLED = False


class dev_config(Config):
    DEBUG = True
    TESTING = True
    #LOGIN_DISABLED = False


