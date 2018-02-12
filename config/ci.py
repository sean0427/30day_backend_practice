"""Configure file for ci"""""
TESTING = True
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'postgres://ubuntu:@127.0.0.1:5432/circle_test?client_encoding=utf8'
