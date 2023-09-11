# -*- coding: utf-8 -*-
{
    "name": "Mindala pruebas",
    "icon": "mindala/static/description/icon.png",
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
    "depends": ["website_partner"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/mindala_templates.xml",
        "views/res_config_settings_views.xml",
        "views/mindala_author/background_view.xml",
        "views/mindala_author/relation_view.xml",
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