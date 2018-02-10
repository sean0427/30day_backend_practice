#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import jsonify

TEST_ID = 1
TEST_DATA = dict(
        name='TEST_NAME',
        address='TEST_ADDRESS',
        telephone='000-0000',
        contant_person_name='jack',
        )

TEST_SECOND_NAME = 'test22'

def assert_response_data(reponse):
    """ check test data in reponse data"""
    data = reponse.get_data(as_text=True) 
    for key, value in TEST_DATA.items():
        assert value in data 
    
def test_get_empty_companies(app):
    reponse = app.get('api/companies', follow_redirects=True)

    assert reponse.status_code == HTTPStatus.OK, 'read success alway ok.'
    assert reponse.get_data(as_text=True) == '[]\n', 'Test Companies, empty list.'

def test_get_company_not_found(app):
    reponse = app.get('api/companies/{}'.format(TEST_ID), follow_redirects=True)

    assert reponse.status_code == HTTPStatus.NOT_FOUND, 'Get Company not found.'
    assert reponse.get_data(as_text=True) == '',  'Test get Companies.'

def test_create_companie(app):
    reponse = app.post('api/companies', data = TEST_DATA, follow_redirects=True)
    
    assert reponse.status_code == HTTPStatus.CREATED, 'Create Companies status code.'
    assert_response_data(reponse)


def test_get_companies(app):
    reponse = app.get('api/companies', follow_redirects=True)

    assert reponse.status_code == HTTPStatus.OK, 'Get list of Companies status code.'
    assert_response_data(reponse)

def test_get_company(app):
    reponse = app.get('api/companies/{}'.format(TEST_ID), follow_redirects=True)

    assert reponse.status_code == HTTPStatus.OK, 'Get Company status code.'
    assert_response_data(reponse)

def test_update_company(app):
    data = TEST_DATA
    data['name'] = TEST_SECOND_NAME


def test_delete_company(app):
    reponse = app.delete('api/companies/{}'.format(TEST_ID), follow_redirects=True)
    
    assert reponse.status_code == HTTPStatus.NO_CONTENT, 'Delete companies status code.'

    data = reponse.get_data(as_text=True) 
    assert not data, 'session delete will return empty'

    reponse = app.get('api/companies', follow_redirects=True)

    assert reponse.status_code == HTTPStatus.OK
    assert reponse.get_data(as_text=True) == '[]\n'
