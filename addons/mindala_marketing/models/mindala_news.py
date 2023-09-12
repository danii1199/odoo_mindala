import logging

from odoo import models, api

from odoo.addons.http_routing.models.ir_http import slug

_logger = logging.getLogger(__name__)


class MindalaNews(models.Model):
    _name = "mindala.news"
    _description = "Mindala news"
    _inherit = ["mindala.base", "mindala.author_rel_abs"]

    @api.model
    def _get_comodel_name(self):
        return self._name

    def _compute_website_url(self):
        super(MindalaNews, self)._compute_website_url()
        for news in self:
            news.website_url = "/news/%s" % (slug(news))
