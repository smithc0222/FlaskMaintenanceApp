#default config

class BaseConfig(object):
    DEBUG = False
    SECRET_KEY='something'
    SQLALCHEMY_DATABASE_URI='sqlite:///posts.db'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
