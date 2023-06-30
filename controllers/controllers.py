# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from odoo.http import serialize_exception


class ScanerControl(http.Controller):
    @http.route('/scaner/products', type='http', auth='public', methods=['GET'])
    def get_products(self, **kwargs):
        products = request.env['product.product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'name': product.name,
                'description': product.description,
                'price': product.list_price,
            })
        return json.dumps(product_data)

    @http.route('/scaner/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}
