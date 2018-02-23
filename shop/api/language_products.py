#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import request, jsonify

from . import api_orm_helper as helper
from . import api, auth

from shop.model.LanguageProduct import LanguageProduct

def exact_request(json, product=None):
    product_id = json['product_id']
    language_id = json['language_id']
    name = json['name']
    describe = json['describe']
    image = json['image']

    if not product:
        return LanguageProduct(product_id, language_id, name, describe, image)

    product.product_id = product_id or product.product_id
    product.language_id = language_id or product.language_id
    product.name = name or product.name
    product.describe = describe or product.describe
    product.image = image or product.image

    return product

@api.route('/language_products', methods=['GET'])
def get_list_of_langnague_products():
    return helper.select_all(LanguageProduct)

@api.route('/language_products', methods=['POST'])
@auth.login_required
def create_language_product():
    return helper.append(exact_request(request.json))

@api.route('/language_products/<id>', methods=['GET'])
def get_language_product(id):
    product = helper.select_by_id(LanguageProduct, id)

    if product:
        return jsonify(product.serialize()), HTTPStatus.OK

    return helper.not_found()

@api.route('/language_products/<id>', methods=['PUT', 'DELETE'])
@auth.login_required
def modify_language_product(id):
    product = helper.select_by_id(LanguageProduct, id)

    if not product:
        return helper.not_found()
    elif request.method == 'DELETE':
        return helper.delete(product)
    elif request.method == 'PUT':
        product = exact_request(request.json, product)
        return helper.update(product)

    return helper.bad_request()
