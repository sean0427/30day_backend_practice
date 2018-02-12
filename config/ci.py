import os

"""Configure file for ci"""""
TESTING = True
DEBUG = True

user = os.getenv('db_user', '')
password = os.getenv('db_passwore', '')
db_name = os.getenv('db_name', '')

SQLALCHEMY_DATABASE_URI = \
        'postgresql://{username}:{password}@{hostname}:{port}/{database}?client_encoding={charset}'\
        .format(
                username=user,
                password=password,
                hostname='127.0.0.1',
                port='5432',
                database=db_name,
                charset='utf8'
        )

SECRET_KEY = os.getenv('SECRET_KEY', 'secrey_key')
