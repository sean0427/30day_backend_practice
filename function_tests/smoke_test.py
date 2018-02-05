#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from selenium import webdriver
from shop import app

def test_smoke():
    """ Test test tool pytest work"""
    assert 1 + 1 == 2

def test_selenium_start():
    """ Test selenium install, and server work"""
    browser = webdriver.Firefox()
    browser.get('http://127.0.0.1:5000')

    #Test has body tag.
    pre = browser.find_elements_by_tag_name('body')
    assert len(pre) != 0, 'check not empty list'

    browser.quit()
