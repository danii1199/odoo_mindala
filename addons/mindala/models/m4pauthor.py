import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class M4PAuthor(models.Model):
    _name = "mindala.m4pauthor"
    _description = "Autores Mindala"

    name = fields.Char(string="Nombre")
    partner_id = fields.Many2one(
        comodel_name="res.partner",
        inverse_name="id",
        string="Contacto",
        required=False,
    )


class M4PAuthorRel(models.Model):
    _name = "mindala.m4pauthor_rel"

    source_model_id = fields.Char(string="Modelo", required=False)
    source_id = fields.Integer(string="ID orígen", required=False)
    type = fields.Selection(
        string="Tipo",
        selection=[
            ("0", "Autor"),
            ("1", "Enlace"),
        ],
        required=False,
    )
    author_id = fields.Many2one(
        comodel_name="mindala.m4pauthor",
        inverse_name="id",
        string="Autor",
        required=False,
    )
    name = fields.Char(string="Nombre", required=False)
    url = fields.Char(string="Url", required=False)
    email = fields.Char(string="Correo", required=False)
    font = fields.Char(string="Fuente", required=False)


class M4PAuthorAbs(models.AbstractModel):
    _name = "mindala.m4pauthor_abs"

    rel_id = fields.One2many(
        comodel_name="mindala.m4pauthor_rel",
        inverse_name="source_id",
        string="Relacion",
        required=False,
    )

    # def write(self, vals):
    #     result = True
    #     _logger.critical(vals)
    #     for fields in vals:
    #         if fields == "rel_id":
    #             for fields_rel in vals[fields]:
    #                 fields_rel[2]["source_model_id"] = self._name
    #                 fields_rel[2]["source_id"] = self.id
    #     result &= super(M4PAuthorAbs, self).write(vals)
    #     return result
