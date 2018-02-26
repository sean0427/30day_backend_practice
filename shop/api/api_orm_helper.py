#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import jsonify

from shop import db

def examime_error(func):
    """ when query fail, return bad request"""
    def with_try(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as err:
            print(err)
            db.session.rollback()
            return bad_request()
    return with_try

@examime_error
def append(model):
    db.session.add(model)
    db.session.commit()

    return jsonify(model.serialize()), HTTPStatus.CREATED

@examime_error
def delete(model):
    db.session.delete(model)
    db.session.commit()

    return jsonify(model.serialize()), HTTPStatus.NO_CONTENT

@examime_error
def update(model):
    db.session.commit()
    return jsonify(model.serialize()), HTTPStatus.CREATED

@examime_error
def select_all(cls):
    return jsonify([ model.serialize() for model in db.session.query(cls).all() ]),\
            HTTPStatus.OK


def not_found():
    return jsonify(), HTTPStatus.NOT_FOUND

def bad_request():
    return jsonify(), HTTPStatus.BAD_REQUEST

def select_by_id(cls, id):
    return db.session.query(cls)\
            .filter(cls.id == id)\
            .one_or_none()

def select_by_field(cls, field, value):
    return db.session.query(cls)\
            .filter(field == value)\
            .one_or_none()
