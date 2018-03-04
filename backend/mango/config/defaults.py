class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'insecure-secret-key'

class ProductionConfig(Config):
    SECRET_KEY = None

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://mango:postgres@postgres:5432/mango'

class TestingConfig(Config):
    TESTING = True
