# -*- coding: utf-8 -*-
{
    "name": "Música",
    "icon": "music/static/description/icon.png",
    "icon_image": "music/static/description/icon.png",
    "summary": """
       """,
    "description": """
        Módulo de canciones
    """,
    "installable": False,
    "author": "Dani's",
    "website": "https://www.youtube.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "website",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "web", "website_partner"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/songs.xml",
        "views/artists.xml",
        "views/snippets/snipet_filter.xml",
        "views/snippets/snipet_templates.xml",
        "views/snippets/snippet.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "assets": {
        "website.assets_wysiwyg": [],
        "website.assets_editor": [],
        "web.assets_tests": [],
        "web.assets_frontend": [],
    },
}
