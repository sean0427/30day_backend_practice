#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, Text

from .BaseModel import BaseModel

class Language(BaseModel):
    __tablename__ = 'language'

    name = Column(Text, nullable=False)
    code = Column(Text(6), nullable=False, unique=True)

    def __init__(self, name, code):
        self.name = name
        self.code = code

    def __iter__(self):
        yield 'name', self.name
        yield 'code', self.code
