#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text

from .BaseModel import BaseModel

class UserClassification(BaseModel):
    __tablename__ = 'user_classification'

    name = Column(Text(10), nullable=False, unique=True)

    def __init__(self, name):
        self.name = name

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
