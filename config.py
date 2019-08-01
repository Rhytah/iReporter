import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    SECRET_KEY = b'\xc9$,\xa9\xdd;\xfeVz\xa0\x8f\xd5A,\x11\xf8\xf4\xceh\x94\xa9\x13\x80['
    SECRET_KEY = os.getenv('SECRET_KEY', 'somewea')
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    DATABASE_URI = os.getenv('DATABASE_URL')
    PORT = 5432


class DevelopmentConfig(Config):
    DEBUG=True
    ENV = 'development'
    DATABASE_URI = 'report_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE_URI = 'reporttest_db'
    TESTING = True

class ProductionConfig(Config):
    DEBUG=False
    ENV = 'production'
    DATABASE_URI= 'postgres://kuzegimbnbuwlw:858f7dd5363a48d534a4184fbe9c3ee5daeadfaf88b73c3267b2aceb92f915b0@ec2-50-16-197-244.compute-1.amazonaws.com:5432/dfktg48dd4p22l'
    DB = 'dfktg48dd4p22l'
    HOST = 'ec2-50-16-197-244.compute-1.amazonaws.com'
    USER = 'kuzegimbnbuwlw'
    PASSWORD='858f7dd5363a48d534a4184fbe9c3ee5daeadfaf88b73c3267b2aceb92f915b0'
    


app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}

