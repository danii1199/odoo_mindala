import logging

from odoo import models, fields

from odoo.addons.http_routing.models.ir_http import slug

_logger = logging.getLogger(__name__)


class MindalaNews(models.Model):
    _name = "mindala.news"
    _description = "Mindala news"
    _inherit = ["mindala.base"]

    authors = fields.One2many(
        comodel_name="mindala.author_rel",
        inverse_name="source_id",
        string="Authors",
        domain=[("source_model_name", "=", _name)],
    )

    videos = fields.One2many(
        comodel_name="mindala.video_rel",
        inverse_name="source_id",
        string="Videos",
        domain=[("source_model_name", "=", _name)],
    )
    tab = fields.Boolean(string="Tab", compute="_mostrate_tab", store=False)

    def _mostrate_tab(self):
        _logger.critical("ESTOY ENTRANDO")
        parameter_name = "mindala_news_authors"
        config_parameter = (
            self.env["ir.config_parameter"].sudo().get_param(parameter_name)
        )
        self.tab = config_parameter
        _logger.critical(config_parameter)

    def _compute_website_url(self):
        super(MindalaNews, self)._compute_website_url()
        for news in self:
            news.website_url = "/news/%s" % (slug(news))
