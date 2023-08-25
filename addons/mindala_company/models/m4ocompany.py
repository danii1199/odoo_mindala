from odoo import api, models, fields, _
from odoo.addons.http_routing.models.ir_http import slug, unslug

class MindalaCompany(models.Model):
    _name = "mindala.m4ocompany"
    _description = "Mindala empresas"
    _inherit = "mindala.default"

    def _compute_website_url(self):
        super(MindalaCompany, self)._compute_website_url()
        for m4ocompany in self:
            m4ocompany.website_url = "/empresas/%s" % (slug(m4ocompany))