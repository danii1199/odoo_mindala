# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons.http_routing.models.ir_http import slug

class Songs(models.Model):
    _name = 'music.songs'
    _description = 'music.songs'

    name = fields.Char(string="Nombre")
    artists = fields.Many2many(string="Artistas",comodel_name = "music.artists")
    record = fields.Char(string="Álbum")
    image = fields.Binary(string="Foto")
