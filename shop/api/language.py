#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import request, jsonify

from . import api_orm_helper as helper
from . import api

from shop.model.Language import Language

@api.route('/language', methods=['GET'])
def language():
    return helper.select_all(Language)
