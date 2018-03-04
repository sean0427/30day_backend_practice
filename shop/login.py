#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from flask import g, jsonify
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

from shop.model.Number import Number
from . import db, app, auth

DEFUALT_EXPIRE_SECOND = 600

TIME_FORMAT = '%Y-%m-%d %H:%M:%S%z'

def verify_auth_token(token):
    s = Serializer(app.config['SECRET_KEY'])

    try:
        data = s.loads(token)
    except SignatureExpired:
        return None # valid token, but expired
    except BadSignature:
        return None # invalid token

    return db.session.query(Number).get(data['id'])

@auth.verify_password
def verify(email_or_token, password):
    user = verify_auth_token(email_or_token)

    if not user:
        user = db.session.query(Number).filter(Number.e_mail == email_or_token).one_or_none()

        if not user or not user.verify_password(password):
            return False

    g.user = user
    return True

def generate_auth_token(user, expiration = DEFUALT_EXPIRE_SECOND):
    """
    generate JSON Web token
    """
    if isinstance(user, Number):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        expire_time = datetime.now() + timedelta(seconds=DEFUALT_EXPIRE_SECOND)

        return s.dumps({
            'id': user.id,
            'user_email': g.user.e_mail,
            'expire_time': expire_time.strftime(TIME_FORMAT),
            })

@app.route('/token')
@auth.login_required
def get_auth_token():
    token = generate_auth_token(g.user)

    return jsonify({ 'token': token.decode('ascii') })
