from odoo import models, fields, api

class Artists(models.Model):
    _name = 'music.artists'
    _description = 'music.artists'

    name = fields.Char(string="Nombre Profesional")
    last_name = fields.Char(string="Apellido")
    first_name = fields.Char(string="Nombre")
    age = fields.Char(string="Edad")
    image = fields.Binary(string="Foto")
    personal_data = fields.Char(compute="_compute_name", string="Nombre y apellidos")
    songs = fields.Many2many(string="Canciones",comodel_name = "music.songs")
    
    def _compute_name(self):
        for data in self:
            data.personal_data = data.first_name + " " + data.last_name