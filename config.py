import os

class Config:
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    JWT_ACCESS_TOKEN_EXPIRES = False
    JWT_TOKEN_LOCATION = ['headers']
    JWT_HEADER_NAME = 'Authorization'
    JWT_HEADER_TYPE = 'Bearer'
    DATABASE_URI = os.getenv('DATABASE_URL')
    

class DevelopmentConfig(Config):
    DEBUG=True
    ENV = 'development'
    DATABASE = 'report_db'
    TESTING = False


class TestingConfig(Config):
    DEBUG=True
    ENV = 'testing'
    DATABASE = 'reporttest_db'
    TESTING = True

class ProductionConfig(Config):
    DEBUG=False
    ENV = 'production'
    DATABASE_URI= 'postgres://wkmnrsrpffhfpr:dde675f7f5af4dc53de4bbac1c7109921fa99454935ce281b3e94798c98eb125@ec2-54-227-246-152.compute-1.amazonaws.com:5432/degbph26bv6m4i'
    DATABASE = "degbph26bv6m4i" 
    HOST = "ec2-54-227-246-152.compute-1.amazonaws.com" 
    PASSWORD ="dde675f7f5af4dc53de4bbac1c7109921fa99454935ce281b3e94798c98eb125"
    USER = "wkmnrsrpffhfpr"
    PORT = 5432
    TESTING= False

app_configuration = {
    "development":DevelopmentConfig,
    "testing":TestingConfig,
    "production":ProductionConfig
}

