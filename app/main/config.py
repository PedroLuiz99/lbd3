import os
from pathlib import Path
from dotenv import load_dotenv

_ENV_FILE = os.path.join(Path(__file__).parent.parent.parent, '.env')

if os.path.isfile(_ENV_FILE):
    load_dotenv(dotenv_path=_ENV_FILE)
else:
    raise Exception("ERROR: env file not found")


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_super_secret_key')
    APP_IP = os.getenv('APP_IP', 5000)
    APP_PORT = os.getenv('APP_PORT', '127.0.0.1')


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DB_URI', os.getenv('DB_URI'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB_URI', os.getenv('DB_URI'))
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DB_URI')


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
