import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class M4PAuthor(models.Model):
    _name = "mindala.m4pauthor"
    _description = "Autores Mindala"

    name = fields.Char(string="Name")
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        inverse_name="id",
        string="Contact",
        required=False,
    )


class M4PAuthorRel(models.Model):
    _name = "mindala.m4pauthor_rel"

    source_model_id = fields.Char(string="Model")
    source_id = fields.Integer(string="Source ID")
    type = fields.Selection(
        string="Type",
        selection=[
            ("0", "Author"),
            ("1", "Link"),
        ],
        default="0",
        required=True,
    )
    author_id = fields.Many2one(
        comodel_name="mindala.m4pauthor",
        inverse_name="id",
        string="Author",
        required=False,
    )
    name = fields.Char(string="Name", required=False)
    url = fields.Char(string="Url", required=False)
    email = fields.Char(string="Email", required=False)
    font = fields.Char(string="Font", required=False)
