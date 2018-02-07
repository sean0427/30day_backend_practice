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

    def test_company(self, session):
        company = Company('name', 'somewhere' , '000-00000', 'jack')

        session.add(company)
        session.commit()

        result = session.query(Company).all()

        assert len(result) == 1
        assert result[0] == company, '{}'.format(company)

    def test_product(self, session):
        product = Product(1, 1)

        session.add(product)
        session.commit()

        result = session.query(Product).all()

        assert len(result) == 1
        assert result[0] == product, '{}'.format(product)

    def test_language_product(self, session):
        product = LanguageProduct(1, 1, 'name', 'describe', 'image')

        session.add(product)
        session.commit()

        result = session.query(LanguageProduct).all()

        assert len(result) == 1
        assert result[0] == product, '{}'.format(product)

    def test_language(self, session):
        language = Language('en', 'English')

        session.add(language)
        session.commit()

        result = session.query(Language).all()

        assert len(result) == 1
        assert result[0] == language, '{}'.format(language)
