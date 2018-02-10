#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from sqlalchemy import Column, Integer, Text

from .BaseModel import BaseModel

class Company(BaseModel):
    __tablename__ = 'company'

    name = Column(Text, nullable=False, unique=True)
    address = Column(Text)
    telephone = Column(Text(10))
    contant_person_name = Column(Text(10))

    def __init__(self, name, address, telephone, contant_person_name):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.contant_person_name = contant_person_name

    def __iter__(self):
        yield 'id', self.id
        yield 'name', self.name
        yield 'address', self.address
        yield 'telephone', self.telephone
        yield 'contant_person_name', self.contant_person_name
