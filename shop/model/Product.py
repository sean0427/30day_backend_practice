#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text, ForeignKey

from .BaseModel import BaseModel
from .Company import Company
from .ProductType import ProductType

class Product(BaseModel):
    __tablename__ = 'product'

    type_id = Column(Integer, ForeignKey('product_type.id'), nullable=False)
    manufacturing = Column(Integer, ForeignKey('company.id'))

    def __init__(self, type_id, manufacturing):
        self.type_id = type_id
        self.manufacturing = manufacturing

    def __iter__(self):
        yield 'id', self.id
        yield 'type_id', self.type_id
        yield 'manufacturing', self.manufacturing
