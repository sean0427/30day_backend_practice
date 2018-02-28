#!/usr/bin/env python
# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import jsonify

from shop import db
from . import api_orm_helper as helper

from shop.model.Product import Product
from shop.model.LanguageProduct import LanguageProduct
from shop.model.DiscountedLocateProduct import DiscountedLocateProduct
from shop.model.LocaleProduct import LocaleProduct

USER_CLASS_NORMAL = 1
DEFAULT_DISCOUNT = 1

find_language_product = lambda product_id, language_id:\
    db.select.query(LanguageProduct)\
    .filter(LanguageProduct.language_id == language_id)\
    .filter(LanguageProduct.product_id == product_id)\
    .one_or_none()

find_locale_product = lambda product_id, locale_id:\
    db.select.query(LanguageProduct)\
    .filter(LocaleProduct.locale_id == locale_id)\
    .filter(LocaleProduct.product_id == product_id)\
    .one_or_none()

find_disconunt_product = lambda locale_product_id, user_classification:\
    db.select.query(DiscountedLocateProduct)\
    .filter(DiscountedLocateProduct.locale_product_id == locale_product_id)\
    .filter(DiscountedLocateProduct.user_classification == user_classification)\
    .one_or_none()\

format_prodcut_information\
    = lambda product, language_product,\
    locale_product, discounted_locate_product:\
        dict(
                discounted_product_id = discounted_locate_product.id,
                name = language_product.name,
                describe = language_product.describe,
                image = language_product.image,
                price = str(locale_product.price),
                discount = discounted_locate_product.discount,
                product_id = product.id,
                )

@helper.examime_error
def select(
        language_id,
        locale_id,
        user_classification_id = USER_CLASS_NORMAL
        ):

    query_result = db.session.query(Product)\
                .join(LocaleProduct)\
                .join(LanguageProduct)\
                .join(DiscountedLocateProduct)\
                .filter(LanguageProduct.language_id == language_id)\
                .filter(LocaleProduct.locale_id == locale_id)\
                .add_entity(LanguageProduct)\
                .add_entity(LocaleProduct)\
                .add_entity(DiscountedLocateProduct)\
                .from_self()\
                .all()

    result = [format_prodcut_information(information[0], information[1],\
                                        information[2], information[3])\
                                        for information in query_result]
    return jsonify(result), HTTPStatus.OK


@helper.examime_error
def insert_new(
        product_type, manufacturing_id,
        language_id, name, describe, image,
        locale_id, price, publisher_id,
        start_datetime, end_datetime
        ):

    product = Product(product_type, manufacturing_id)

    db.session.add(product)
    db.session.flush()

    language_product = LanguageProduct(product.id, language_id, name, describe, image)
    db.session.add(language_product)
    db.session.flush()

    locale_product = LocaleProduct(product.id, locale_id, price, publisher_id)
    db.session.add(locale_product)
    db.session.flush()

    discounted_product = DiscountedLocateProduct(
            locale_product.id, USER_CLASS_NORMAL, DEFAULT_DISCOUNT,
            start_datetime, end_datetime)
    db.session.add(discounted_product)

    db.session.commit()

    result = format_prodcut_information(
            product, language_product, locale_product, discounted_product)
    return jsonify(result), HTTPStatus.CREATED


@helper.examime_error
def delete():
    pass

@helper.examime_error
def update():
    pass
