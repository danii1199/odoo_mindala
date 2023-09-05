import logging

from odoo import models, fields

from odoo.addons.http_routing.models.ir_http import slug

_logger = logging.getLogger(__name__)


class MindalaNews(models.Model):
    _name = "mindala.news"
    _description = "Mindala news"
    _inherit = ["mindala.base"]

    authors = fields.One2many(
        comodel_name="mindala.m4pauthor_rel",
        inverse_name="source_id",
        string="Relacion",
        domain=[("source_model_id", "=", _name)],
    )

    def _compute_website_url(self):
        super(MindalaNews, self)._compute_website_url()
        for news in self:
            news.website_url = "/news/%s" % (slug(news))
