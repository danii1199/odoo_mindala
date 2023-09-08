# -*- coding: utf-8 -*-
{
    "name": "Mindala Noticias",
    "icon": "mindala_news/static/description/icon.png",
    "icon_image": "mindala/static/description/icon.png",
    "summary": """
       Mindala Framework""",
    "description": """
        Aplicación de Mindala con multiples tipos de datos
    """,
    "author": "dmanzano",
    "website": "https://www.mindalatech.com",
    "installable": False,
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Website/Website",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["website_partner", "mindala"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/m4pnews_back_views.xml",
        "views/m4pnews_add.xml",
        "views/m4pnews_templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        # 'demo/demo.xml',
    ],
    "assets": {
        "website.assets_wysiwyg": [],
        "website.assets_editor": [
            "mindala_news/static/src/js/tours/mindala_news.js",
            "mindala_news/static/src/js/systray_items/*.js",
        ],
        "web.assets_tests": [],
        "web.assets_frontend": [],
    },
}
