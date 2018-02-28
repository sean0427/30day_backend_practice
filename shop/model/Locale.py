#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Text

from .BaseModel import BaseModel

class Locale(BaseModel):
    __tablename__ = 'locale'

    name = Column(Text)

    def __init__(self, name):
       self.name = name 
    
    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
