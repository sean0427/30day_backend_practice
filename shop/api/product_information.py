#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from http import HTTPStatus
from flask import request, jsonify

from . import orm_product_information_helper as helper
from . import api, auth

TIME_FORMAT = '%Y-%m-%d %H:%M:%S' 

@api.route('/product_info', methods=['GET'])
def get_product_information():
    language_id = request.args.get('language', default=1, type=int)
    locale_id = request.args.get('locale', default=1, type=int)

    return helper.select(language_id, locale_id)

@api.route('/product_info', methods=['POST'])
@auth.login_required
def create_new_prodct_info():
    json = request.json 

    product_type = json.get('product_type')
    manufacturing_id = json.get('manufacturing')
    language_id = json.get('language')
    name = json.get('name')
    describe = json.get('describe')
    image = json.get('image')
    locale_id = json.get('locale')
    price = json.get('price')
    publisher_id = json.get('publisher')
    start_datetime = datetime.strptime(json.get('start_datetime'), TIME_FORMAT)
    end_datetime = datetime.strptime(json.get('end_datetime'), TIME_FORMAT)
        
    return helper.insert_new(
        product_type, manufacturing_id,
        language_id, name, describe, image,
        locale_id, price, publisher_id,
        start_datetime, end_datetime
        )

@api.route('/product_info/<id>', methods=['DELETE'])
@auth.login_required
def delete_product_info():
    pass
