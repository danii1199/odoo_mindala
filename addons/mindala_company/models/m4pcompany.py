import logging

from odoo import models

from odoo.addons.http_routing.models.ir_http import slug

_logger = logging.getLogger(__name__)


class MindalaCompany(models.Model):
    _name = "mindala.m4pcompany"
    _description = "Mindala empresas"
    _inherit = ["mindala.base", "mindala.m4pauthor_abs"]

    def _compute_website_url(self):
        super(MindalaCompany, self)._compute_website_url()
        for m4pcompany in self:
            m4pcompany.website_url = "/empresas/%s" % (slug(m4pcompany))

    # def get_authors(self):
    #     query = "SELECT * FROM mindala_m4pauthor_rel"
    #     self.env.cr.execute(query)
    #     line_ids = list(line[0] for line in self.env.cr.fetchall())
    #
    #     return {
    #         "type": "ir.actions.act_window",
    #         "name": "Salida autores",
    #         "view_type": "form",
    #         "view_mode": "tree,pivot",
    #         "res_model": "mindala.m4pcompany",
    #         "domain": [("id", "in", line_ids)],
    #     }
