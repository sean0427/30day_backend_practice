#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, ForeignKey, Numeric

from .BaseModel import BaseModel
from .Product import Product
from .Company import Company 
from .Locale import Locale

class LocaleProduct(BaseModel):
    __tablename__ = 'locale_product'

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    locale_id = Column(Integer, ForeignKey('locale.id'), nullable=False)
    price = Column(Numeric, nullable=False)
    publisher = Column(Integer, ForeignKey('company.id'), nullable=False)

    def __init__(self, product_id, locale_id, price, publisher):
        self.product_id = product_id
        self.locale_id = locale_id
        self.price = price
        self.publisher = publisher

    def __iter__(self):
        yield 'id', self.id
        yield 'product_id', self.product_id
        yield 'locale_id', self.locale_id
        yield 'price', self.price
        yield 'publisher', self.publisher
