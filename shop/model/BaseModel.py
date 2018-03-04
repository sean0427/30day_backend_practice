#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import Column, Integer

from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.ext.declarative import declarative_base

class SerializeMixin():
    """
    Class Serialze Tool
    implement class.__iter__ to use it

    """
    def serialize(self):
        return dict(self)

class _BaseModel(SerializeMixin):
    __abstract__ = True

    id = Column(Integer, primary_key=True, nullable=False, unique=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower();

    def __repr__(self):
       """
       Define model print,
       """
       return '%s(%s)' % (\
               self.__class__.__name__,
               {
                   column: value
                   for column, value in dict(self).items()
                   }
               )

    def __eq__(self, other):
        return isinstance(other, self.__class__) and other.id == self.id

BaseModel = declarative_base(cls=_BaseModel)
