from odoo import models, fields

from odoo.addons.http_routing.models.ir_http import slug


class MindalaCompany(models.Model):
    _name = "mindala.m4pcompany"
    _description = "Mindala empresas"
    _inherit = ["mindala.base"]

    rel_id = fields.One2many(
        comodel_name="mindala.m4pauthor_rel",
        inverse_name="source_id",
        string="Relacion",
        domain=[("source_model_id", "=", _name,
    )

    def _compute_website_url(self):
        super(MindalaCompany, self)._compute_website_url()
        for m4pcompany in self:
            m4pcompany.website_url = "/empresas/%s" % (slug(m4pcompany))
