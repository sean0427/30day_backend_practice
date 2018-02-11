#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import jsonify, request

from . import api

from shop.model.Company import Company
from . import api_orm_helper as helper

def exact_request(json, company = None):
    name = json['name']
    address = json['address']
    telephone = json['telephone']
    contant_person_name = json['contant_person_name']

    if not company:
        return Company(name, address, telephone, contant_person_name)

    company.name = name or company.name
    company.address = address or company.address
    company.telephone = telephone or company.telephone
    company.contant_person_name = contant_person_name or company.contant_person_name

    return company

@api.route('/companies', methods=['GET', 'POST'])
def companies():
    if request.method == 'POST':
        return helper.append(exact_request(request.json))

    return helper.select_all(Company)

@api.route('/companies/<id>', methods=['GET', 'PUT', 'DELETE'])
def company(id):
    company = helper.select_by_id(Company, id)

    if not company:
        return helper.not_found()

    if request.method == 'GET':
        return jsonify(company.serialize()), HTTPStatus.OK
    elif request.method == 'PUT':
        return helper.update(exact_request(request.json, company))
    elif request.method == 'DELETE':
        return helper.delete(company)

    return helper.bad_request()
