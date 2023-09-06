# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    mindala_news_authors = fields.Boolean(string="Authors")
    mindala_news_videos = fields.Boolean(string="Videos")

    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "mindala_news_authors", self.mindala_news_authors
        )
        self.env["ir.config_parameter"].sudo().set_param(
            "mindala_news_videos", self.mindala_news_videos
        )
        return res

    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        author = self.env["ir.config_parameter"].get_param("mindala_news_authors")
        video = self.env["ir.config_parameter"].get_param("mindala_news_videos")
        res.update(
            {"mindala_news_authors": author, "mindala_news_videos": video},
        )
        return res
