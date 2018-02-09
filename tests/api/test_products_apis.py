#!/usr/bin/env python
# -*- coding: utf-8 -*-

TEST_TEXT = 'test'
TEST_ID = 1

def test_echo(app):
    reponse = app.get('api/echo/{}'.format(TEST_TEXT), follow_redirects=True)
    
    assert TEST_TEXT in reponse.get_data(as_text=True), 'Test Echo'

def test_get_products(app):
    reponse = app.get('api/products', follow_redirects=True)

    assert reponse.get_data(as_text=True) == '[]\n', 'Test Products.'

def test_get_product(app):
    reponse = app.get('api/products/{}'.format(TEST_ID), follow_redirects=True)

    assert reponse.get_data(as_text=True) == '{}\n',  'Test get Product.'
