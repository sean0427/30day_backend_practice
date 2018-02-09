#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, ForeignKey

from .BaseModel import BaseModel
from .Product import Product
from .Language import Language

class LanguageProduct(BaseModel):
    __tablename__ = 'language_product'

    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    language_id = Column(Integer, ForeignKey('language.id'), nullable=False)
    name = Column(Text(100), nullable=False)
    describe = Column(Text)
    image = Column(Text(100))

    def __init__(self, product_id, language_id, name, describe, image):
        self.product_id = product_id
        self.language_id = language_id
        self.name = name
        self.describe = describe
        self.image = image

    def __iter__(self):
        yield 'product_id', self.product_id
        yield 'language_id', self.language_id
        yield 'name', self.name
        yield 'describe', self.describe
        yield 'image', self.image
