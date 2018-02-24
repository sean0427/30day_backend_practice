import os
import pytest
import tempfile

from flask import g

import shop
from shop.model.BaseModel import BaseModel
from shop.model.Number import Number
from consts import TEST_USER_DATA
MEMORY_ENGINE = 'sqlite:///:memory:'

def create_number():
    number = Number(TEST_USER_DATA['password'], TEST_USER_DATA['email'], 1)
    shop.db.session.add(number)
    shop.db.session.commit()

    return number

@pytest.fixture(scope='module')
def app():
    shop.app.config['SQLALCHEMY_DATABASE_URI'] = MEMORY_ENGINE
    shop.app.testing = True

    BaseModel.metadata.create_all(shop.db.engine)

    try:
        create_number()
    except:
        print('err')

    yield shop.app.test_client()

    shop.db.session.remove()
    shop.db.drop_all()
