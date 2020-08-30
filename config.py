class Config(object):
    DEBUG = False
    TESTING = False

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pgroot@localhost/guerreiro'

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
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:pgroot@localhost/gr_teste'

