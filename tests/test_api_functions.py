#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from http import HTTPStatus

TEST_TEXT = 'TEXT'
EMPTY_JSON_ARRAY = '[]\n'

CONTENT_TYPE = 'application/json'

DATA = dict(
        email = 'test@test.com',
        password = 'passworddd'
)

def test_echo(app):
    response = app.get('api/echo/{}'.format(TEST_TEXT), follow_redirects=True)
    assert TEST_TEXT in response.get_data(as_text=True), 'Test Echo'

def test_product_type_api(app):
    response = app.get('api/product_type', follow_redirects=True)
    assert EMPTY_JSON_ARRAY == response.get_data(as_text=True), 'Test Product Type'

def test_user_register(app):
    response = app.post(
            'api/users', data=json.dumps(DATA),
            follow_redirects=True, content_type=CONTENT_TYPE
            )
    
    assert response.status_code == HTTPStatus.CREATED, 'Create new user.'

    response = app.post(
            'api/users', data=json.dumps(DATA),
            follow_redirects=True, content_type=CONTENT_TYPE
            )
    
    assert response.status_code == HTTPStatus.BAD_REQUEST, 'Inert twice will fail.'
