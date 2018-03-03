#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask.views import MethodView
from flask import jsonify, request
from . import auth 

from . import api_orm_helper as helper

from shop.model.Product import Product as klass 

def examime_error(func):
    """ when query fail, return bad request"""
    def with_try(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)
            db.session.rollback()
            return bad_request()
    return with_try

class API(MethodView):
    def exact_request(self, json, product=None):
        type_id = json['type_id']
        manufacturing = json['manufacturing']

        if not product:
            return klass(type_id, manufacturing)

        product.type_id = type_id or product.type_id
        product.manufacturing = manufacturing or product.manufacturing
        return product

    def get(self, id):
        if id is None:
            return helper.select_all(klass)

        model = helper.select_by_id(klass, id)

        if not model:
            return helper.not_found();

        return jsonify(model.serialize()), HTTPStatus.OK

    @auth.login_required
    def post(self):
        model = self.exact_request(request.json)

        if isinstance(model, klass):
            return helper.append(model)

        return helper.bad_request()

    @auth.login_required
    def delete(self, id):
        model = helper.select_by_id(klass, id)

        if not model:
            return helper.not_found();

        if request.method == 'DELETE':
            return helper.delete(model)

        return helper.bad_request()

    @auth.login_required
    def put(self, id):
        model = helper.select_by_id(klass, id)

        if not model:
            return helper.not_found();

        if request.method == 'PUT':
            model = self.exact_request(request.json, model)
            return helper.update(model)

        return helper.bad_request()
