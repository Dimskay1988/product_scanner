# -*- coding: utf-8 -*-
{
    'name': "Scanner product",

    'summary': """
        Module for providing products via HTTP request""",

    'description': """
        Long description of module's purpose
    """,

    'author': "5sControl",
    'website': "https://eigsoft.com/5scontrol",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/security.xml',
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        # 'views/idle_control_menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3'
}
