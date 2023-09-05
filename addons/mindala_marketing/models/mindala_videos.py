import logging

from odoo import models, fields

from odoo.addons.http_routing.models.ir_http import slug

_logger = logging.getLogger(__name__)


class MindalaVideos(models.Model):
    _name = "mindala.videos"
    _description = "Mindala videos"
    _inherit = ["mindala.base"]

    authors = fields.One2many(
        comodel_name="mindala.m4pauthor_rel",
        inverse_name="source_id",
        string="Relacion",
        domain=[("source_model_id", "=", _name)],
    )

    def _compute_website_url(self):
        super(MindalaVideos, self)._compute_website_url()
        for videos in self:
            videos.website_url = "/videos/%s" % (slug(videos))
