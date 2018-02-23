#!/usr/bin/env python
# -*- coding: utf-8 -*-

from passlib.apps import custom_app_context as pwd_context
from sqlalchemy import Column, Integer, Text

from .BaseModel import BaseModel

class Number(BaseModel):
    __tablename__ = 'number'

    password = Column(Text, nullable=False)
    e_mail = Column(Text, nullable=False, unique=True)
    user_classification_id = Column(Integer, nullable=False)

    def __init__(self, password, e_mail, user_classification_id):
        self.hash_password(password)
        self.e_mail = e_mail
        self.user_classification_id = user_classification_id

    def get_id(self):
        return self.e_mail

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def __iter__(self):
        yield 'id', self.id
        yield 'e_mail', self.e_mail
