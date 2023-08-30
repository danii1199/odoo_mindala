from odoo import api, models, fields, _
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website.tools import text_from_html
from odoo.tools.json import scriptsafe as json_scriptsafe
from odoo.tools.translate import html_translate

class M4PBase(models.AbstractModel):
    _name = "mindala.base"
    _description = "Mindala Defecto"
    _inherit = ['website.seo.metadata', 'website.published.multi.mixin',
        'website.cover_properties.mixin', 'website.searchable.mixin']
    _order = 'id DESC'

    def _default_content(self):
        return '''
            <p class="o_default_snippet_text">''' + _("Start writing here...") + '''</p>
        '''
    name = fields.Char('Title', required=True, translate=True, default='')
    subtitle = fields.Char('Sub Title', translate=True)
    author_id = fields.Many2one('res.partner', 'Author', default=lambda self: self.env.user.partner_id)
    author_avatar = fields.Binary(related='author_id.image_128', string="Avatar", readonly=False)
    author_name = fields.Char(related='author_id.display_name', string="Author Name", readonly=False, store=True)
    active = fields.Boolean('Active', default=True)
    content = fields.Html('Content', default=_default_content, translate=html_translate, sanitize=False)

    create_date = fields.Datetime('Created on', readonly=True)
    published_date = fields.Datetime('Published Date')
    post_date = fields.Datetime('Publishing date', compute='_compute_post_date', inverse='_set_post_date', store=True,
                                help="The blog post will be visible for your visitors as of this date on the website if it is set as published.")
    create_uid = fields.Many2one('res.users', 'Created by', readonly=True)
    write_date = fields.Datetime('Last Updated on', readonly=True)
    write_uid = fields.Many2one('res.users', 'Last Contributor', readonly=True)

    @api.depends('create_date', 'published_date')
    def _compute_post_date(self):
        for default in self:
            if default.published_date:
                default.post_date = default.published_date
            else:
                default.post_date = default.create_date

    def _set_post_date(self):
        for default in self:
            default.published_date = default.post_date
            if not default.published_date:
                default.post_date = default.create_date

    def _check_for_publication(self, vals):
        if vals.get('is_published'):
            return True
        return False

    def write(self, vals):
        result = True
        if 'active' in vals and not vals['active']:
            vals['is_published'] = False
        for post in self:
            copy_vals = dict(vals)
            published_in_vals = set(vals.keys()) & {'is_published', 'website_published'}
            if (published_in_vals and 'published_date' not in vals and
                    (not post.published_date or post.published_date <= fields.Datetime.now())):
                copy_vals['published_date'] = vals[list(published_in_vals)[0]] and fields.Datetime.now() or False
            result &= super(M4PBase, post).write(copy_vals)
        self._check_for_publication(vals)
        return result
