#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from sqlalchemy import Text, Column, Integer, TIMESTAMP, ForeignKey

from .BaseModel import BaseModel
from .LocaleProduct import LocaleProduct
from .UserClassification import UserClassification

class DiscountedLocateProduct(BaseModel):
    __tablename__ = 'discounted_locate_product'

    locale_product_id = Column(Integer, ForeignKey('locale_product.id'), nullable=False)
    user_classification_id = Column(Integer, ForeignKey('user_classification.id'), nullable=False)
    discount = Column(Integer, nullable=False)
    start_datetime = Column(TIMESTAMP, nullable=False)
    end_datetime = Column(TIMESTAMP, nullable=False)

    def __init__(
            self, locale_product_id,
            user_classification_id, discount,
            start_datetime, end_datetime):
        self.locale_product_id = locale_product_id
        self.user_classification_id = user_classification_id
        self.discount = discount
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime

    def __iter__(self):
        yield 'name', self.name
        yield 'locale_product_id', self.locale_product_id
        yield 'user_classification_id', self.user_classification_id
        yield 'discount', self.discount
        yield 'start_datetime', self.start_datetime
        yield 'end_datetime', self.end_datetime
