from flask import request

from shop import app, db
from shop.model.LanguageProduct import LanguageProduct

@app.route('/api/echo/<string:argument>', methods=['get', 'post'])
def echo(argument):
    """ basic api argument test, for check api is work"""
    return argument

@app.route('/api/products', methods=['GET'])
def get_list_of_products():
    page = request.args.get('page', default=1, type=int)
    limited = request.args.get('limited', default=1, type=int)
    lng = request.args.get('lng', default=0, type=int)

    products = db.session.query(LanguageProduct)\
        .filter(LanguageProduct.language_id == lng)\
        .all()

    return '{}'.format(products)

@app.route('/api/product/<id>', methods=['GET', 'POST'])
def get_product(id):
    lng = request.args.get('lng', default=0, type=int)
    product = db.session.query(LanguageProduct)\
        .filter(LanguageProduct.product_id == id)\
        .filter(LanguageProduct.language_id == lng)\
        .one_or_none()

    return product if product else ''
