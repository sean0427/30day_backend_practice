#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__, instance_relative_config=True)

running_config = os.getenv('APP_RUNNING_ENV', '')

if running_config == 'CI':
    app.config.from_object('config.ci')
elif running_config == 'DEV':
    app.config.from_object('config.dev')
else:
    app.config.from_object('config.default')

print('running config file {}'.format(running_config))

app.config.from_pyfile('config.py', silent=True)

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

#views
import shop.index
import shop.login

#blueprint
from shop.api import api

app.register_blueprint(api, url_prefix='/api')
