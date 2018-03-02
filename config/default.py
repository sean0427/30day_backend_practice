import os

TESTING = False
DEBUG = False
SQLALCHEMY_ECHO = False

DB_URL = os.getenv('DB_URL')

SQLALCHEMY_DATABASE_URI = \
        'postgresql://{db_url}?client_encoding=urf8'.format(db_url=db_url)

SECRET_KEY = os.getenv('SECRET_KEY')
