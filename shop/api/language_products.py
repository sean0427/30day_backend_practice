#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .api_klass import create_api_method_view, register_api_view_method
from shop.model.LanguageProduct import LanguageProduct

def exact(json, product=None):
    product_id = json['product_id']
    language_id = json['language_id']
    name = json['name']
    describe = json['describe']
    image = json['image']

    if not product:
        return LanguageProduct(product_id, language_id, name, describe, image)

    product.product_id = product_id or product.product_id
    product.language_id = language_id or product.language_id
    product.name = name or product.name
    product.describe = describe or product.describe
    product.image = image or product.image

    return product

view_method = create_api_method_view(exact, LanguageProduct)
products_view = view_method.as_view('language_products_api')
register_api_view_method('language_products', products_view)
