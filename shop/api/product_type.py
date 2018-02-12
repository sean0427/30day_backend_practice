#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import jsonify, request

from . import api

from shop.model.ProductType import ProductType
from . import api_orm_helper as helper

@api.route('/product_type', methods=['GET'])
def product_type():
    return helper.select_all(ProductType)
