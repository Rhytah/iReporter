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
    DEBUG = True
    ENV = 'development'
    DATABASE_URI = 'report_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG = True
    ENV = 'testing'
    DATABASE_URI = 'reporttest_db'
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    DATABASE_URI = 'postgres://srwsecjayzimxz:75cfbe00ffc5c2424d5662afa29f31b7c8ce2e4a8b2fb77ac7297ca1253389c5@ec2-174-129-226-234.compute-1.amazonaws.com:5432/daih072tt5nqcp'
    DB = 'daih072tt5nqcp'
    HOST = 'ec2-174-129-226-234.compute-1.amazonaws.com'
    USER = 'srwsecjayzimxz'
    PASSWORD = '75cfbe00ffc5c2424d5662afa29f31b7c8ce2e4a8b2fb77ac7297ca1253389c5'


app_configuration = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
