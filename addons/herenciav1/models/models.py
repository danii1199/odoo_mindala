# -*- coding: utf-8 -*-

from odoo import models, fields

class Songs(models.Model):
    _inherit = "music.songs"
    
    duration = fields.Char(string="Duración")
    