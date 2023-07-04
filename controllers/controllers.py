# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json


class ScanerControl(http.Controller):
    @http.route('/scaner/products', type='http', auth='public', methods=['GET'])
    def get_products(self, **kwargs):
        products = request.env['product.product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.list_price,
                'default_code': product.default_code,
            })
        return json.dumps(product_data)

    @http.route('/scaner/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}
