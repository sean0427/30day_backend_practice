#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .api_klass import create_api_method_view, register_api_view_method
from shop.model.Product import Product

def exact_function(json, product = None):
    type_id = json['type_id']
    manufacturing = json['manufacturing']

    if not product:
        return Product(type_id, manufacturing)

    product.type_id = type_id or product.type_id
    product.manufacturing = manufacturing or product.manufacturing
    return product


view_method = create_api_method_view(exact_function, Product)
products_view = view_method.as_view('products_api')
register_api_view_method('products', products_view)
