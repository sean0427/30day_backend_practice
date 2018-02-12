#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import request, jsonify

from . import api_orm_helper as helper
from . import api

from shop.model.Product import Product

def exact_request(json, product=None):
    type_id = json['type_id']
    manufacturing = json['manufacturing']

    if not product:
        return Product(type_id, manufacturing)

    product.type_id = type_id or product.type_id
    product.manufacturing = manufacturing or product.manufacturing

    return product

@api.route('/products', methods=['GET', 'POST'])
def get_list_of_products():
    page = request.args.get('page', default=1, type=int)
    limited = request.args.get('limited', default=1, type=int)

    if request.method == 'POST':
        return helper.append(exact_request(request.json))

    return helper.select_all(Product)

@api.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_product(id):
    product = helper.select_by_id(Product, id)

    if not product:
        return helper.not_found()

    if request.method == 'GET':
        return jsonify(product.serialize()), HTTPStatus.OK
    elif request.method == 'DELETE':
        return helper.delete(product)
    elif request.method == 'PUT':
        product = exact_request(request.json, product)
        return helper.update(product)

    return helper.bad_request()
