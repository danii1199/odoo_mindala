# -*- coding: utf-8 -*-
{
    'name': "odoo_view_advanced",

    'summary': """
        Conceptos avanzados de vistas""",

    'description': """
        Curso de conceptos avanzados de vistas
    """,

    'author': "Daniel Manzano Díaz",
    'website': "https://www.udemy.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'odoo_view_advanced/demo.xml',
    ],
    'assets': {
    'web.assets_qweb': [
        'odoo_view_advanced/static/src/xml/button.xml',
    ],
    'web.assets_backend': [
        'odoo_view_advanced/static/src/js/action_call.js',
    ],
},
}
