#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import request, jsonify

from . import api_orm_helper as helper
from . import api

from .api_klass import API

products_view = API.as_view('products_api')

api.add_url_rule('/products/', defaults={'id': None},
                         view_func=products_view, methods=['GET',])
api.add_url_rule('/products', view_func=products_view, methods=['POST',])
api.add_url_rule('/products/<int:id>', view_func=products_view,
                         methods=['GET', 'PUT', 'DELETE'])
