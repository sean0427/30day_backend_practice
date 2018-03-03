#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import request, jsonify

from . import api_orm_helper as helper
from . import api

from .api_klass import create_api_method_view
from shop.model.Product import Product

def exact_function(json, product=None):
    type_id = json['type_id']
    manufacturing = json['manufacturing']

    if not product:
        return Product(type_id, manufacturing)

    product.type_id = type_id or product.type_id
    product.manufacturing = manufacturing or product.manufacturing
    return product


view_method = create_api_method_view(exact_function, Product)
products_view = view_method.as_view('products_api')

api.add_url_rule('/products/', defaults={'id': None},
                         view_func=products_view, methods=['GET',])
api.add_url_rule('/products', view_func=products_view, methods=['POST',])
api.add_url_rule('/products/<int:id>', view_func=products_view,
                         methods=['GET', 'PUT', 'DELETE'])
