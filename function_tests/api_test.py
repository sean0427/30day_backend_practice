#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver

URL_LIST = [
        'http://127.0.0.1:5000',
        'http://127.0.0.1:5000/login'
        ]

class TestAPI:
    @pytest.fixture(scope='function', params=URL_LIST)
    def driver(self, request):
        driver = webdriver.Firefox() 
        driver.get(request.param)

        def fin():
            """ teardown """
            driver.quit()

        print("Test URL {}".format(request.param))
        return driver 

    def test_api_basic(self, driver):
        pre = driver.find_elements_by_tag_name('body')
        assert len(pre) != 0, 'check not empty list'
