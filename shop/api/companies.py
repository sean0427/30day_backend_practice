#!/usr/bin/env python
# -*- coding: utf-8 -*-


from .api_klass import create_api_method_view, register_api_view_method
from shop.model.Company import Company

def exact(json, company = None):
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

view_method = create_api_method_view(exact, Company)
products_view = view_method.as_view('company_api')
register_api_view_method('companies', products_view)
