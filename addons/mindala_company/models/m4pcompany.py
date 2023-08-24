from odoo import api, models, fields, _
from odoo.addons.http_routing.models.ir_http import slug, unslug

class M4PCompany(models.Model):
    _name = "mindala.m4pcompany"
    _description = "Mindala empresas"
    _inherit = "mindala.default"