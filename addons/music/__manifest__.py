# -*- coding: utf-8 -*-
{
    'name': "Música",
    'icon': 'music/static/description/icon.png',
    'icon_image': 'music/static/description/icon.png',

    'summary': """
       """,

    'description': """
        Módulo de canciones
    """,

    'author': "Dani's",
    'website': "https://www.youtube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web', 'website_partner'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/songs.xml',
        'views/artists.xml',
        'views/snipet_filter.xml',
        'views/snipet_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
