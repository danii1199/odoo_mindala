# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
import werkzeug
import itertools
import pytz
import babel.dates
from collections import OrderedDict

from odoo import http, fields, tools
from odoo.addons.http_routing.models.ir_http import slug, unslug
from odoo.addons.website.controllers.main import QueryURL
from odoo.addons.portal.controllers.portal import _build_url_w_params
from odoo.http import request
from odoo.osv import expression
from odoo.tools import html2plaintext
from odoo.tools.misc import get_lang
from odoo.tools import sql

class WebsiteNews(http.Controller):
    _blog_post_per_page = 10

    @http.route([
        '''/blog/noticias-<int:id_blog>/<model("blog.m4pnews", "[('blog_id','=',blog.id)]"):blog_m4pnews>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def blog_m4pnews(self,id_blog,blog_m4pnews,tag_id=None,page=1,enable_editor=None, **post):
        blog = request.env['blog.blog'].browse(int(id_blog))
        BlogPost = request.env['blog.m4pnews']
        date_begin, date_end = post.get('date_begin'), post.get('date_end')

        domain = request.website.website_domain()
        blogs = blog.search(domain, order="create_date, id asc")

        tag = None
        if tag_id:
            tag = request.env['blog.tag'].browse(int(tag_id))
        blog_url = QueryURL('', ['blog', 'tag'], blog=blog_m4pnews.blog_id, tag=tag, date_begin=date_begin, date_end=date_end)

        if not blog_m4pnews.blog_id.id == blog.id:
            return request.redirect("/blog/%s/%s" % (slug(blog_m4pnews.blog_id), slug(blog_m4pnews)), code=301)

        tags = request.env['blog.tag'].search([])

        # Find next Post
        blog_m4pnews_domain = [('blog_id', '=', blog.id)]
        if not request.env.user.has_group('website.group_website_designer'):
            blog_m4pnews_domain += [('post_date', '<=', fields.Datetime.now())]

        all_post = BlogPost.search(blog_m4pnews_domain)

        if blog_m4pnews not in all_post:
            return request.redirect("/blog/%s" % (slug(blog_m4pnews.blog_id)))

        # should always return at least the current post
        all_post_ids = all_post.ids
        current_blog_post_index = all_post_ids.index(blog_m4pnews.id)
        nb_posts = len(all_post_ids)
        next_post_id = all_post_ids[(current_blog_post_index + 1) % nb_posts] if nb_posts > 1 else None
        next_post = next_post_id and BlogPost.browse(next_post_id) or False

        values = {
            'tags': tags,
            'tag': tag,
            'blog': blog,
            'blog_post': blog_m4pnews,
            'blogs': blogs,
            'main_object': blog_m4pnews,
            # 'nav_list': self.nav_list(blog),
            'enable_editor': enable_editor,
            'next_post': next_post,
            'date': date_begin,
            'blog_url': blog_url,
        }
        response = request.render("mindala.blog_post_complete", values)

        if blog_m4pnews.id not in request.session.get('posts_viewed', []):
            if sql.increment_fields_skiplock(blog_m4pnews, 'visits'):
                if not request.session.get('posts_viewed'):
                    request.session['posts_viewed'] = []
                request.session['posts_viewed'].append(blog_m4pnews.id)
                request.session.touch()
        return response 


    @http.route([
        '''/blog/noticias-<int:id_blog>''',
    ], type='http', auth="public", website=True, sitemap=True)
    def blog(self, id_blog=None, tag=None, page=1, search=None, **opt):
        Blog = request.env['blog.blog']
        blog = request.env['blog.blog'].browse(int(id_blog))
        if isinstance(blog, str):
            blog = Blog.browse(int(re.search(r'\d+', blog)[0]))
            if not blog.exists():
                raise werkzeug.exceptions.NotFound()

        blogs = tools.lazy(lambda: Blog.search(request.website.website_domain(), order="create_date asc, id asc"))

        if not blog and len(blogs) == 1:
            url = QueryURL('/blog/%s' % slug(blogs[0]), search=search, **opt)()
            return request.redirect(url, code=302)

        date_begin, date_end, state = opt.get('date_begin'), opt.get('date_end'), opt.get('state')

        if tag and request.httprequest.method == 'GET':
            # redirect get tag-1,tag-2 -> get tag-1
            tags = tag.split(',')
            if len(tags) > 1:
                url = QueryURL('' if blog else '/blog', ['blog', 'tag'], blog=blog, tag=tags[0], date_begin=date_begin, date_end=date_end, search=search)()
                return request.redirect(url, code=302)

        values = self._prepare_blog_values(blogs=blogs, blog=blog, date_begin=date_begin, date_end=date_end, tags=tag, state=state, page=page, search=search)

        # in case of a redirection need by `_prepare_blog_values` we follow it
        if isinstance(values, werkzeug.wrappers.Response):
            return values

        if blog:
            values['main_object'] = blog
            values['blog_url'] = QueryURL('', ['blog', 'tag'], blog=blog, tag=tag, date_begin=date_begin, date_end=date_end, search=search)
        else:
            values['blog_url'] = QueryURL('/blog', ['tag'], date_begin=date_begin, date_end=date_end, search=search)

        return request.render("mindala.blog_post_short", values)