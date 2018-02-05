#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

uri = 'http://127.0.0.1:5000'

class TestLoginPage:
    @pytest.fixture(scope="function")
    def driver(self, request):
        driver = webdriver.Firefox()
        yield driver
        driver.quit()

    def test_login(self, driver):
        """Test login Behavior"""
        driver.get(uri)
        driver.find_element(By.LINK_TEXT, 'log in').click()
        
        driver.implicitly_wait(5)
        form = driver.find_element(By.TAG_NAME, 'form')
        assert form, 'find form'

        input_username = form.find_element(By.NAME, 'username')
        input_password = form.find_element(By.NAME, 'password')
        input_submit = form.find_element(By.NAME, 'submit')

        #TODO find password
        input_username.send_keys('test@test.test')
        input_password.send_keys('admin')
        input_submit.send_keys(Keys.ENTER)

        driver.implicitly_wait(5)
        link = driver.find_element(By.LINK_TEXT,'log out')
        assert link, 'check login seuccess'
        link.click()

        
