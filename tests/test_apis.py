#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

APIS = [
        dict(path='companies', data=TEST_COMPANIES_DATA),
        dict(path='products', data=TEST_PRODUCT_DATA)
]

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

    yield
    #not do anything on teardwon

@pytest.mark.usefixture('api_param')
class TestAPIS:
    """ To test shop/api/*"""

    def assert_response_data(self, response):
        """ check test data in response data"""
        data = response.get_data(as_text=True)
        for key, value in self.data.items():
            assert str(value) in data

    def test_get_empty_mutil(self):
        response = self.app.get(self.path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK, 'read success alway ok.'
        assert response.get_data(as_text=True) == '[]\n', 'Test empty list.'

    def test_get_company_not_found(self):
        response = self.app.get(self.single_path, follow_redirects=True)

        assert response.status_code == HTTPStatus.NOT_FOUND, 'Get not found.'
        assert response.get_data(as_text=True) == '',  'Test get '

    def test_create(self):
        response = self.app.post(self.path, data=self.data, follow_redirects=True)

        assert response.status_code == HTTPStatus.CREATED, 'Create status code.'
        self.assert_response_data(response)


    def test_get_mutil(self):
        response = self.app.get(self.path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK, 'Get list of Companies status code.'
        self.assert_response_data(response)

    def test_get(self):
        response = self.app.get(self.single_path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK, 'Get status code.'
        self.assert_response_data(response)

    def test_update(self):
        pass

    def test_delete(self):
        response = self.app.delete(self.single_path, follow_redirects=True)

        assert response.status_code == HTTPStatus.NO_CONTENT, 'Delete status code.'

        data = response.get_data(as_text=True)
        assert not data, 'session delete will return empty'

        response = self.app.get(self.path, follow_redirects=True)

        assert response.status_code == HTTPStatus.OK
        assert response.get_data(as_text=True) == '[]\n'
