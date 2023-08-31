from odoo import fields, models


class ModelName(models.Model):
    _name = "mindala.m4pauthor"
    _description = "Autores Mindala"

    name = fields.Char(string="nombre")
    partner = fields.One2many(
        comodel_name="res.partner",
        inverse_name="id",
        string="Contactos",
        required=False,
    )
