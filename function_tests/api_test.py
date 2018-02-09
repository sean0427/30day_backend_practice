#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver

ROOT = 'http://127.0.0.1:5000/api/'

URL_LIST = [
        'products',
        'product/1'
]

class TestAPI:
    @pytest.fixture(scope='function', params=URL_LIST)
    def driver(self, request):
        driver = webdriver.Firefox() 
        driver.get('{}/{}'.format(ROOT, request.param))

        yield driver

        #teardown
        driver.quit()

    def test_api_basic(self, driver):
        pre = driver.find_elements_by_tag_name('body')
        assert len(pre) != 0, 'check not empty list'
