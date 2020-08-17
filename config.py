class Config(object):
    DEBUG = False
    TESTING = False

    DB_SERVER = "localhost"
    # DB_NAME = "guerreiro"
    DB_NAME = "gr_teste"
    DB_USERNAME = "postgres"
    DB_PASSWORD = "pgroot"

    SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_SERVER + '/' + DB_NAME

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = 'development'
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
