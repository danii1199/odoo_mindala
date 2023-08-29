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
        '''/empresas/<model("mindala.m4pcompany"):m4pcompany>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def blog_post(self, m4pcompany):
        values = {
            "m4pcompany" : m4pcompany,
            'main_object': m4pcompany,
        }
        response = request.render("mindala_company.m4pcompany_complete", values)
        return response
    
    @http.route(['''/empresas'''], type='http', auth="public", website=True, sitemap=True)
    def get_companies(self, limit='15'):
        values = { }
        values['m4pcompanies'] = request.env['mindala.m4pcompany'].search([])
        response = request.render("mindala_company.m4pcompany_list", values)
        return response