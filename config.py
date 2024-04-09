import os 
from dotenv import load_dotenv

app_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv()


class BaseConfig:
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopementConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_DATABASE_URI')
    TEMPLATES_AUTO_RELOAD = True
    
    
class TestingConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URI')
class ProductionConfig(BaseConfig):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_DATABASE_URI')
    
    
config = dict(
    development=DevelopementConfig,
    testing=TestingConfig,
    production=ProductionConfig
)

def get_config():
    flask_env = os.environ.get('FLASK_ENV')
    # default to development
    print(" * FLASK_ENV: " + flask_env)
    return config.get(flask_env)