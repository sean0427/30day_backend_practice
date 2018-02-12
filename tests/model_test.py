#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from shop.model.BaseModel import BaseModel
from shop.model.Language import Language
from shop.model.Company import Company
from shop.model.Product import Product
from shop.model.ProductType import ProductType
from shop.model.LanguageProduct import LanguageProduct

MEMORY_ENGINE = 'sqlite:///:memory:'

MODLES = [
        Company('name', 'somewhere' , '000-00000', 'jack'),
        Product(1, 1),
        LanguageProduct(1, 1, 'name', 'describe', 'image'),
        Language('en', 'English'),
        ProductType('name')
]


class TestModel():
    """ Test Models create, select and insert"""

    @pytest.fixture(scope="function")
    def session(self, request):
        engine = create_engine(MEMORY_ENGINE)
        BaseModel.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        yield session

        BaseModel.metadata.drop_all(engine)

    @pytest.fixture(scope="module", params=MODLES)
    def model(self, request):
        return request.param

    def test_add_model(self, session, model):
        session.add(model)
        session.commit()

        result = session.query(model.__class__).all()

        assert len(result) == 1
        assert result[0] == model, '{}'.format(product)
        assert dict(model)
