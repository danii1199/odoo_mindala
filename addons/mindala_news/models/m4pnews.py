import logging

from odoo import models, fields

from odoo.addons.http_routing.models.ir_http import slug

_logger = logging.getLogger(__name__)


class MindalaNews(models.Model):
    _name = "mindala.m4pnews"
    _description = "Mindala noticias"
    _inherit = ["mindala.base"]

    rel_id = fields.One2many(
        comodel_name="mindala.m4pauthor_rel",
        inverse_name="source_id",
        string="Relacion",
        domain=[("source_model_id", "=", _name)],
    )

    def _compute_website_url(self):
        super(MindalaNews, self)._compute_website_url()
        for m4pnews in self:
            m4pnews.website_url = "/noticias/%s" % (slug(m4pnews))

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
