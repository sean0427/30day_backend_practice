#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, Blueprint
from flask_httpauth import HTTPBasicAuth

from shop import auth

api = Blueprint('api', __name__)

from . import users
from . import products
from . import companies
from . import language_products
from . import product_type
from . import language
from . import product_information


@api.route('/echo/<string:argument>', methods=['GET', 'POST'])
def echo(argument):
    """ basic api argument test, for check api is work"""
    return argument

@api.route('/login_echo/<string:argument>', methods=['GET', 'POST'])
@auth.login_required
def login_echo(argument):
    """ basic api argument test, for check api is work"""
    return argument
