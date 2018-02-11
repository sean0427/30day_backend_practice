#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pytest
from http import HTTPStatus

#data
TEST_ID = 1
TEST_TEXT = 'TEXT'

TEST_COMPANIES_DATA = dict(
        name='TEST_NAME',
        address='TEST_ADDRESS',
        telephone='000-0000',
        contant_person_name='jack',
        )

TEST_PRODUCT_DATA = dict(type_id=1, manufacturing=1)
CONTENT_TYPE = 'application/json'

APIS = [
        dict(path='companies', data=TEST_COMPANIES_DATA, update_key='name', update_value=TEST_TEXT),
        dict(path='products', data=TEST_PRODUCT_DATA, update_key='type_id', update_value=2)
]

#consts
EMPTY_JSON_ARRAY = '[]\n'
EMPTY_JSON = '{}\n'

def test_echo(app):
    response = app.get('api/echo/{}'.format(TEST_TEXT), follow_redirects=True)
    assert TEST_TEXT in response.get_data(as_text=True), 'Test Echo'

@pytest.fixture(scope='class', params=APIS, autouse=True)
def api_param(request, app):
    if request.cls is not None:
        """ set varivable to class"""
        request.cls.app = app
        request.cls.path = 'api/{}'.format(request.param['path'])
        request.cls.single_path = 'api/{}/{}'.format(request.param['path'], TEST_ID)
        request.cls.data = request.param['data']
        #TODO workaround
        request.cls.update_key = request.param['update_key']
        request.cls.update_value = request.param['update_value']

    yield
    #not do anything on teardwon

@pytest.mark.usefixture('api_param')
class TestAPIS:
    """ To test shop/api/*"""

    def assert_response_data(self, response=None, data=None, new_data=None):
        """ check test data in response data"""

        new_data = new_data or self.data

        if not data:
            if response:
                data = json.loads(response.get_data(as_text=True))
            else:
                assert false

        for key in self.data.keys():
            assert data[key] == new_data[key]

    def test_get_empty_mutil(self):
        response = self.app.get(self.path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK, 'read success alway ok.'
        assert response.get_data(as_text=True) == EMPTY_JSON_ARRAY, 'Test empty list.'

    def test_get_by_id_not_found(self):
        response = self.app.get(self.single_path, follow_redirects=True)

        assert response.status_code == HTTPStatus.NOT_FOUND, 'Get not found.'
        assert response.get_data(as_text=True) == EMPTY_JSON, 'Test get '

    def test_create(self):
        response = self.app.post(
                self.path, data=json.dumps(self.data),
                follow_redirects=True, content_type=CONTENT_TYPE
                )

        assert response.status_code == HTTPStatus.CREATED, 'Create status code.'
        self.assert_response_data(response)

    def test_get_mutil(self):
        response = self.app.get(self.path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK, 'Get list of Companies status code.'
        result = json.loads(response.get_data(as_text=True))
        self.assert_response_data(data=result[0])

    def test_get(self):
        response = self.app.get(self.single_path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK, 'Get status code.'
        self.assert_response_data(response)

    def test_update(self):
        """ TODO workaround update key and value save on class"""
        new_data = self.data
        new_data[self.update_key] = self.update_value

        response = self.app.put(
                self.single_path, data=json.dumps(self.data),
                follow_redirects=True, content_type=CONTENT_TYPE
                )

        assert response.status_code == HTTPStatus.CREATED, 'Update status code.'
        self.assert_response_data(response, new_data=new_data)

    def test_delete(self):
        response = self.app.delete(self.single_path, follow_redirects=True)

        assert response.status_code == HTTPStatus.NO_CONTENT, 'Delete status code.'

        data = response.get_data(as_text=True)
        assert not data, 'session delete will return empty'

        response = self.app.get(self.path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK
        assert response.get_data(as_text=True) == EMPTY_JSON_ARRAY
