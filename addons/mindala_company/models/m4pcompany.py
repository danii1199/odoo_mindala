from odoo import api, models, fields, _
from odoo.addons.http_routing.models.ir_http import slug, unslug

class MindalaCompany(models.Model):
    _name = "mindala.m4pcompany"
    _description = "Mindala empresas"
    _inherit = "mindala.base"

    def _compute_website_url(self):
        super(MindalaCompany, self)._compute_website_url()
        for m4pcompany in self:
            m4pcompany.website_url = "/empresas/%s" % (slug(m4pcompany))