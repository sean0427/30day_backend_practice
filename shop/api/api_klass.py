#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask.views import MethodView
from flask import jsonify, request
from . import auth 

from . import api_orm_helper as helper

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

def create_api_method_view(exact_function, klass, helper=helper):
    class API(MethodView):
        def exact_request(self, json, model=None):
            model = exact_function(json, model)

            print(model)
            if isinstance(model, klass):
                return model

            raise TypeError('exact function return wrong type')

        def get(self, id):
            if id is None:
                return helper.select_all(klass)

            model = helper.select_by_id(klass, id)

            if model:
                return jsonify(model.serialize()), HTTPStatus.OK

            return helper.not_found();

        @auth.login_required
        def post(self):
            return helper.append(self.exact_request(request.json))

        @auth.login_required
        def delete(self, id):
            model = helper.select_by_id(klass, id)

            if model:
                return helper.delete(model)

            return helper.not_found();

        @auth.login_required
        def put(self, id):
            model = helper.select_by_id(klass, id)

            if model:
                return helper.update(self.exact_request(request.json, model))

            return helper.not_found()

    return API
