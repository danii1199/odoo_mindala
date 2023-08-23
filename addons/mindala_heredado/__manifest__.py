# -*- coding: utf-8 -*-
{
    'name': "Mindala Heredado",

    'icon': 'mindala/static/description/icon.png',
    'icon_image': 'mindala/static/description/icon.png',
    
    'summary': """
       Mindala Framework""",

    'description': """
        Aplicación de Mindala con multiples tipos de datos
    """,

    'author': "dmanzano",
    'website': "https://www.mindalatech.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website/Website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web', 'website_partner', 'website_blog'],

    # always loaded
    'data': [
        'views/blog_m4pnews_add.xml',
        'views/website_pages_views.xml',
        'views/website_blog_templates.xml',
        'views/website_blog_posts_loop.xml',
        'views/website_blog_components.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'assets': {
        'website.assets_wysiwyg': [
        ],
        'website.assets_editor': [
            #'mindala/static/src/js/tours/mindala.js',
            'mindala/static/src/js/systray_items/*.js',
        ],
        'web.assets_tests': [
        ],
        'web.assets_frontend': [
        ],
    },
}