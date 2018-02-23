#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import g, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

from shop.model.Number import Number
from . import db, app, auth

DEFUALT_EXPIRE_SECOND = 600

def verify_auth_token(token):
    s = Serializer(app.config['SECRET_KEY'])

    try:
        data = s.loads(token)
    except SignatureExpired:
        return None # valid token, but expired
    except BadSignature:
        return None # invalid token

    return db.session.query(Number).filter(Number.id == data['id']).one_or_none()

def generate_auth_token(user, expiration = DEFUALT_EXPIRE_SECOND):
    if isinstance(user, Number):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'id': user.id })

@auth.verify_password
def verify_password(email_or_token, password):
    user = verify_auth_token(email_or_token)

    if not user:
        user = db.session.query(Number).filter(Number.e_mail == email_or_token).one_or_none()

        if not user or not user.verify_password(password):
            return False

    g.user = user
    return True

@app.route('/token')
@auth.login_required
def get_auth_token():
    token = generate_auth_token(g.user)
    return jsonify({ 'token': token.decode('ascii') })
