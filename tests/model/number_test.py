#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from passlib.apps import custom_app_context as pwd_context

from shop.model.BaseModel import BaseModel
from shop.model.Number import Number

MEMORY_ENGINE = 'sqlite:///:memory:'
TEST_NUMBER_PASSWORD = 'aaa'
TEST_NUMBER_E_MAIL = 'aa@aaa.aa'
NUMBER_CLASS_GOLD = 1

SECOND_PASSWORD = "pa@ss(word1"
SECOND_E_MAIL = "test2@test.test"

SERIAL_FIRST = 1

class TestNumberModel():
    """check number model work, and learn how to use sqlalchemy sesstion"""

    @pytest.fixture(scope="function")
    def session(self, request):
        engine = create_engine(MEMORY_ENGINE)
        BaseModel.metadata.create_all(engine)

        Session = sessionmaker(bind=engine)
        session = Session()

        number = Number(TEST_NUMBER_PASSWORD, TEST_NUMBER_E_MAIL, NUMBER_CLASS_GOLD)
        session.add(number)
        session.commit()

        yield session

        BaseModel.metadata.drop_all(engine)

    def get_default_number(self, session):
        number = session.query(Number).filter(Number.e_mail == TEST_NUMBER_E_MAIL).one_or_none()

        if number:
            return number

        assert False

    def test_select(self, session):
        result = self.get_default_number(session)

        assert not result == None
        assert result.verify_password(TEST_NUMBER_PASSWORD)

    def test_insert(self, session):
        second_number = Number(SECOND_PASSWORD, SECOND_E_MAIL, NUMBER_CLASS_GOLD)

        session.add(second_number)
        session.commit()

        assert second_number.id == SERIAL_FIRST + 1, 'check serial incremnet'

        result = session.query(Number).all()
        default_number = self.get_default_number(session)

        assert len(result) == 2, 'check 2nd number insert'
        assert second_number in result
        assert default_number in result

        #insert twice
        session.add(second_number)
        session.commit()

        result = session.query(Number).all()
        assert len(result) == 2, 'check insert twice'
        assert second_number in result

    def test_delete(self, session):
        number = self.get_default_number(session)

        session.delete(number)
        session.commit()

        result = session.query(Number).all()
        assert len(result) == 0

    def test_update(self, session):
        number = self.get_default_number(session)
        number.e_mail = SECOND_E_MAIL

        session.commit()
        result = session.query(Number).filter(Number.e_mail == number.e_mail).all()

        assert len(result) == 1
        assert result[0] == number
        assert result[0].id == SERIAL_FIRST
