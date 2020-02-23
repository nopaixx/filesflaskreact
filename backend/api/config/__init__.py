import os

class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # you can override this default config or us enviroment vars
    APP_PATH = os.environ.get('APP_PATH','/app/api')
    STATIC_PATH = 'static'
    STATIC_FOLDER = "{}/{}".format(APP_PATH, STATIC_PATH)
    SERVER_NAME_URI = os.environ.get('SERVER_NAME_URI','http://127.0.0.1:8081')
    NOT_FOUND_IMAGE = "{}/{}".format(SERVER_NAME_URI, '/static/404.jpg')
    SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URI",'postgres://demo:demo@postgres/demo')
    ALLOWED_EXTENSIONS = { 'png', 'jpg'}    

    VIRUS_SCAN = False

class ProductionConfig(Config):
    DEBUG = False
    VIRUS_SCAN = True


class StagingConfig(Config):
    DEBUG = True
    VIRUS_SCAN = False


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    VIRUS_SCAN = False


class TestingConfig(Config):
    TESTING = True
    VIRUS_SCAN = False
