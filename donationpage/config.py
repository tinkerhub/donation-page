import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
TOP_LEVEL_DIR = os.path.abspath(os.curdir)

class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('RAZORPAY_KEY_TESTING')
    RAZORPAY_SECRET = os.environ.get('RAZORPAY_SECRET_TESTING')
    TEMPLATES_AUTO_RELOAD = True
    MAILGUN_API_KEY = os.environ.get('MAILGUN_API_KEY')

class ProductionConfig(Config):
    DEBUG=False
    SECRET_KEY = os.environ.get('RAZORPAY_KEY')
    RAZORPAY_SECRET = os.environ.get('RAZORPAY_SECRET')

class StagingConfig(Config):
    DEVELOPMENT=True
    DEBUG=True

class StagingConfig(Config):
    DEVELOPMENT=True
    DEBUG=True

class TestingConfig(Config):
    TESTING=True
    DEBUG=True
    