# -*- coding: utf-8 -*-

from odoo import models, fields

class Music(models.Model):
    _inherit = "music.songs"
    _name = "herenciav1.music"
    
    duration = fields.Char(string="Duración")