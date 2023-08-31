from odoo import fields, models


class M4PAuthor(models.Model):
    _name = "mindala.m4pauthor"
    _description = "Autores Mindala"

    name = fields.Char(string="nombre")
    partner_id = fields.One2many(
        comodel_name="res.partner",
        inverse_name="id",
        string="Contactos",
        required=False,
    )
