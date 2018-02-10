import os
import pytest
import tempfile

import shop
from shop.model.BaseModel import BaseModel

MEMORY_ENGINE = 'sqlite:///:memory:'

@pytest.fixture(scope='module')
def app():
    shop.app.config['SQLALCHEMY_DATABASE_URI'] = MEMORY_ENGINE
    shop.app.testing = True

    BaseModel.metadata.create_all(shop.db.engine)
    yield shop.app.test_client()

    shop.db.session.remove()
    shop.db.drop_all()
