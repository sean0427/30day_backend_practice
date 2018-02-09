#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, Blueprint

api = Blueprint('api', __name__)

from . import products
