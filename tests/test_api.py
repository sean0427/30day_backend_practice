#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shop import api, app

TEST_TEXT = 'test'
TEST_ID = 1


app = app.test_client()

def test_has_module():
    assert api

def test_echo():
    reponse = app.get('api/echo/{}'.format(TEST_TEXT), follow_redirects=True)
    
    assert TEST_TEXT in reponse.get_data(as_text=True), 'Test Echo'

def test_get_products():
    reponse = app.get('api/products', follow_redirects=True)

    assert reponse.get_data(as_text=True) == '[]', 'Test Products.'

def test_get_product():
    reponse = app.get('api/product/{}'.format(TEST_ID), follow_redirects=True)

    assert reponse.get_data(as_text=True) == '',  'Test get Product.'
