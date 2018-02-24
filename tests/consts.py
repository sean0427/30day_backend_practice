#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base64 import b64encode

#data
TEST_ID = 1
TEST_TEXT = 'TEXT'

TEST_PRODUCT_DATA = dict(type_id=1, manufacturing=1)

TEST_LANGUAGE_PRODUCT_DATA = dict(
        product_id = TEST_ID,
        language_id = TEST_ID,
        name = 'TEST_NAME',
        describe = TEST_TEXT,
        image = 'http://testtest.test.jpg'
)

TEST_USER_DATA = dict(
        email = 'log@test.com',
        password = 'padoekjmjjoi123'
)

#consts
EMPTY_JSON_ARRAY = '[]\n'
EMPTY_JSON = '{}\n'
CONTENT_TYPE = 'application/json'

_login_data = b64encode('{}:{}'.format(TEST_USER_DATA['email'], TEST_USER_DATA['password']).encode('utf-8')).decode('ascii')

LOGIN_HEADERS = {
            'Authorization': 'Basic {}'.format(_login_data)
}

if __name__ == '__main__':
    print(LOGIN_HEADERS)

