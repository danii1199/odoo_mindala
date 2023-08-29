# -*- coding: utf-8 -*-
import re
import werkzeug
import itertools
import pytz
import babel.dates
from collections import OrderedDict

from odoo import http, fields, tools
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.portal.controllers.portal import _build_url_w_params
from odoo.http import request
from odoo.osv import expression
from odoo.tools import html2plaintext
from odoo.tools.misc import get_lang
from odoo.tools import sql

class WebsiteBlog(http.Controller):
    @http.route([
        '''/empresas/<model("mindala.m4ocompany"):m4ocompany>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def blog_post(self, m4ocompany):
        values = {
            "m4ocompany" : m4ocompany,
            'main_object': m4ocompany,
        }
        response = request.render("mindala_company.m4ocompany_complete", values)
        return response
    
    @http.route(['''/empresas'''], type='http', auth="public", website=True, sitemap=True)
    def get_companies(self, limit='15'):
        values = { }
        values['m4ocompanies'] = request.env['mindala.m4ocompany'].search([])
        response = request.render("mindala_company.m4ocompany_list", values)
        return response