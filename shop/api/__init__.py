#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, Blueprint

api = Blueprint('api', __name__)

from . import products
from . import companies
from . import language_products
from . import product_type
from . import language

@api.route('/echo/<string:argument>', methods=['GET', 'POST'])
def echo(argument):
    """ basic api argument test, for check api is work"""
    return argument
