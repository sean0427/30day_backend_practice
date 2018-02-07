#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text

from shop.model.BaseModel import BaseModel

class Number(BaseModel):
    __tablename__ = 'number'
    is_active = True
    is_anonymous = False
    is_authenticated = True

    password = Column(Text, nullable=False)
    e_mail = Column(Text, nullable=False, unique=True)
    user_classification_id = Column(Integer, nullable=False)

    def __init__(self, password, e_mail, user_classification_id):
        self.password = password
        self.e_mail = e_mail
        self.user_classification_id = user_classification_id

    def get_id(self):
        return self.e_mail

    def __iter__(self):
        yield 'id', self.id
        yield 'e_mail', self.e_mail
