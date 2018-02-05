from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Number(Base):
    __tablename__ = 'number'
    is_active = True
    is_anonymous = False
    is_authenticated = True

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    e_mail = Column(Text, nullable=False, unique=True)
    user_classification_id = Column(Integer, nullable=False)

    def get_id(self):
        return self.e_mail

    def __repr__(self):
       """Define a base way to print models"""
       return '%s(%s)' % (self.__class__.__name__, {
           column: value
           for column, value in dict(self).items()
           })

    def __iter__(self):
        yield 'id', self.id
        yield 'e_mail', self.e_mail
