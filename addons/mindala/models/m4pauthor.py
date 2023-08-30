from odoo import fields, models


class ModelName(models.Model):
    _name = "mindala.m4pauthor"
    _description = "Autores Mindala"

    name = fields.Char(string="nombre")
