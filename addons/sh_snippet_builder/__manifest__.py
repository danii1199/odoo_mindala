# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Snippet Builder",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "Website",
    "summary": "Snippets Builder Module, Make Snippet, create Website Block, Snnipet Builder Blocks, Snippet Generator, Snipet Build App, snnipet Builder Box, Website Content Box, HTML box, HTML block, css block, js block, HTML Snnipet, HTML Snipet, css block Odoo",
    "description": """You have some technical knowlege about web designing and you want to build some custom snippets for your website? Currently odoo does not provide any snippet where you can type code and design a snippet. so that whay we made this module. It will provide a plateform where you can make design and build a snippets for your websites.
Snippet Builder Odoo
 Snippets Builder Module, Make Snippet, create Website Block, Snnipet Builder Blocks, Snippet Generator, Snipet Build, snnipet Builder Box, Website Content Box, HTML box, HTML block, css block, js block, HTML Snnipet, HTML Snipet, css block, js Box.
 Snippets Builder Module, Make Snippet, create Website Block, Snnipet Builder Blocks, Snippet Generator, Snipet Build App, snnipet Builder Box, Website Content Box, HTML box, HTML block, css block, js block, HTML Snnipet, HTML Snipet, css block, js Box.

""",
    "version": "16.0.1",
    "depends": ["base", "website"],
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/sh_snippet_builder_views.xml",
        "views/sh_snippet_template.xml",
        "data/sh_snippet_data.xml",
        "views/snippet.xml",
    ],
    "assets": {
        "website.assets_wysiwyg": [
            "sh_snippet_builder/static/src/js/website.editor.js",
            "sh_snippet_builder/static/src/xml/sh_snippet_builder_popup.xml",
        ],
    },
    "images": [
        "static/description/background.png",
    ],
    "license": "OPL-1",
    "auto_install": False,
    "installable": True,
    "price": 30,
    "currency": "EUR",
}
