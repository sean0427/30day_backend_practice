#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import jsonify

from shop import db

def append(model):
    db.session.add(model)
    db.session.commit()

    return jsonify(model.serialize()), HTTPStatus.CREATED

def delete(model):
    db.session.delete(model)
    db.session.commit()
    return jsonify(model.serialize()), HTTPStatus.NO_CONTENT

def update(model):
    db.session.update(model)
    db.session.commit()
    return jsonify(model.serialize()), HTTPStatus.CREATED

def select_all(cls):
    return jsonify([ model.serialize() for model in db.session.query(cls).all() ]),\
            HTTPStatus.OK

def select_by_id(cls, id):
    return db.session.query(cls)\
            .filter(cls.id == id)\
            .one_or_none()

def not_found():
    return '', HTTPStatus.NOT_FOUND

def bad_request():
    return '', HTTPStatus.BAD_REQUEST
