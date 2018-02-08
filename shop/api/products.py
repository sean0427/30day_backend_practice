from flask import request, Blueprint, jsonify

from shop import db
from shop.model.LanguageProduct import LanguageProduct

from . import api

@api.route('/echo/<string:argument>', methods=['GET', 'POST'])
def echo(argument):
    """ basic api argument test, for check api is work"""
    return argument

@api.route('/products', methods=['GET'])
def get_list_of_products():
    page = request.args.get('page', default=1, type=int)
    limited = request.args.get('limited', default=1, type=int)
    lng = request.args.get('lng', default=0, type=int)

    products = db.session.query(LanguageProduct)\
        .filter(LanguageProduct.language_id == lng)\
        .all()

    return jsonify(products)

@api.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def get_product(id):
    lng = request.args.get('lng', default=0, type=int)
    product = db.session.query(LanguageProduct)\
        .filter(LanguageProduct.product_id == id)\
        .filter(LanguageProduct.language_id == lng)\
        .one_or_none()

    result = product if product else None

    return jsonify(result)
