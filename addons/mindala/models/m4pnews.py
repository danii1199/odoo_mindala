from odoo import models, fields


class M4PNews(models.Model):
    _name = "blog.m4pnews"
    _inherit = "blog.post"
    
    standfirst = fields.Char(string = "Entradilla")
