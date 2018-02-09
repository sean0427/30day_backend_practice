#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import redirect, request, abort, render_template, flash, url_for
from flask_login import login_required, login_user, logout_user

from shop import app, login_manager, db
from shop.model.Number import Number

@login_manager.user_loader
def load_user(email):
    return db.session.query(Number).filter(Number.e_mail == email).one_or_none()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = load_user(username)

        if user is not None and user.password == password:
            login_user(user)

            #TODO HTTPS
            next = request.args.get('next')
            return redirect(next or url_for('index'))
        else:
            flash('Wrong email or password!')

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return "logout"

@login_manager.unauthorized_handler
def unauthorized_handler():
    flash('unauthorized')
    return redirect(url_for('index'))
