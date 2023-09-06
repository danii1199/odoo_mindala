from odoo import fields, models


class MindalaVideo(models.Model):
    _name = "mindala.video"
    _description = "Mindala Video"

    name = fields.Char(string="Name")


class MindalaVideoRel(models.Model):
    _name = "mindala.video_rel"

    name = fields.Char(string="Name")
    source_model_name = fields.Char(string="Model")
    source_id = fields.Integer(string="Source Id")
