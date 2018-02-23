#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import api
from flask import request

from shop.model.Number import Number
from . import api_orm_helper as helper

DEFAULT_CLASSIFICATION  = 1;

@api.route('/users', methods=['POST'])
def new_user():
    json = request.json

    e_mail = json['email']
    password = json['password']

    if not e_mail or not password:
        return helper.bad_request()

    if helper.select_by_field(Number, Number.e_mail, e_mail) != None:
        return helper.bad_request()

    return helper.append(Number(password, e_mail, DEFAULT_CLASSIFICATION))
