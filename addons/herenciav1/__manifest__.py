# -*- coding: utf-8 -*-
{
    'name': "herencia-v1",

    'summary': """
        Prueba de la primera herencia""",

    'description': """
         Prueba de la primera herencia...  preuba
    """,

    'author': "dmanzano",
    'website': "https://www.mindalatech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','music'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/snipet_templates.xml',
        'reports/visit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
