from odoo import models, fields
from odoo.addons.http_routing.models.ir_http import slug, unslug

class M4PNews(models.Model):
    _name = "blog.m4pnews"
    _inherit = "blog.post"
    
    standfirst = fields.Char(string = "Entradilla")
    
    def _compute_website_url(self):
        super(M4PNews, self)._compute_website_url()
        for blog_m4pnews in self:
            blog_m4pnews.website_url = "/blog/noticias/%s/%s" % (slug(blog_m4pnews.blog_id), slug(blog_m4pnews))
