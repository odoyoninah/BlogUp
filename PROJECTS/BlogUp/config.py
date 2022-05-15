from flask import config
import os

class Config:

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY='4545'
    
    # SECRET_KEY = os.environ.get('SECRET_KEY')

    pass

class ProdConfig(Config):

    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/blog'
    DEBUG = True

class TestConfig(Config):

    pass

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}

