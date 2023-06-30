# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json
from odoo.addons.web.controllers.main import serialize_exception



class IdleControl(http.Controller):
    @http.route('/my_module/products', type='http', auth='public', methods=['GET'])
    @serialize_exception
    def get_products(self, **kwargs):
        products = request.env['product.product'].sudo().search([])
        product_data = []
        for product in products:
            product_data.append({
                'name': product.name,
                'description': product.description,
                'price': product.price,
                # Добавьте все нужные поля продукта в словарь
            })
        return json.dumps(product_data)


    @http.route('/scaner/ping', type='json', auth='public')
    def ping(self):
        return {'success': True}
