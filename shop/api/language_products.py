#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import request, jsonify

from . import api_orm_helper as helper
from . import api

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

@api.route('/language_products', methods=['GET', 'POST'])
def get_list_of_langnague_products():
    if request.method == 'POST':
        return helper.append(exact_request(request.json))

    return helper.select_all(LanguageProduct)

@api.route('/language_products/<id>', methods=['GET', 'PUT', 'DELETE'])
def language_product(id):
    product = helper.select_by_id(LanguageProduct, id)

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
