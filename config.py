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
    DATABASE_URI = 'postgres://postgres:psql@localhost:5432/reporttest_db'
    TESTING = True

class ProductionConfig(Config):
    DEBUG=False
    ENV = 'production'
    DATABASE_URI= 'postgres://wkmnrsrpffhfpr:dde675f7f5af4dc53de4bbac1c7109921fa99454935ce281b3e94798c98eb125@ec2-54-227-246-152.compute-1.amazonaws.com:5432/degbph26bv6m4i'


app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}

