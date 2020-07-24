import os

class Config:
    '''
    General configuration parent class
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:Access@localhost/postblog'
   
    SECRET_KEY = '\x84\x14\x10KH\xfb\xb4\x18\xe6\x08"\x95\x1f4\xda\xa8\xe6\xdb\xaf\xb8]\xc4\xfe5'
    WTF_CSRF_ENABLED = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    
    DEBUG = True

config_options ={"production":ProdConfig,"default":DevConfig}

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}