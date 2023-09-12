import logging

from odoo import fields, models, api

_logger = logging.getLogger(__name__)


class MindalaAuthor(models.Model):
    _name = "mindala.author"
    _description = "Autores Mindala"

    name = fields.Char(string="Name")
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        inverse_name="id",
        string="Contact",
        required=False,
    )


class MindalaAuthorRel(models.Model):
    _name = "mindala.author_rel"

    source_model_name = fields.Char(string="Model")
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
        comodel_name="mindala.author",
        inverse_name="id",
        string="Author",
        required=False,
    )
    name = fields.Char(string="Name", required=False)
    url = fields.Char(string="Url", required=False)
    email = fields.Char(string="Email", required=False)
    font = fields.Char(string="Font", required=False)


class MindalaAuthorRelAbs(models.AbstractModel):
    _name = "mindala.author_rel_abs"

    @api.model
    def _get_comodel_name(self):
        return

    def _get_domain(self):
        comodel_name = self._get_comodel_name()
        return [("source_model_name", "=", comodel_name)]

    authors = fields.One2many(
        comodel_name="mindala.author_rel",
        inverse_name="source_id",
        string="Authors",
        domain=_get_domain,
    )

    def _get_ir_config_parameter_value(self):
        model_name = self._get_comodel_name().replace(".", "_")
        parameter_name = "" f"{model_name}_authors"
        author = self.env["ir.config_parameter"].get_param(parameter_name)
        return author

    author_tab = fields.Boolean(
        string="Mostrate Tab",
        default=lambda self: self._get_ir_config_parameter_value(),
        store=False,
    )
