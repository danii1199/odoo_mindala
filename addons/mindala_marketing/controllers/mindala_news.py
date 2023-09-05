# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class MindalaNews(http.Controller):
    @http.route(
        [
            """/news/<model("mindala.news"):mindala_new>""",
        ],
        type="http",
        auth="public",
        website=True,
        sitemap=True,
    )
    def news(self, mindala_new):
        values = {
            "mindala_new": mindala_new,
            "main_object": mindala_new,
        }
        response = request.render("mindala_marketing.mindala_news_complete", values)
        return response

    @http.route(["""/news"""], type="http", auth="public", website=True, sitemap=True)
    def get_news(self):
        values = {}
        values["mindala_news"] = request.env["mindala.news"].search([])
        response = request.render("mindala-marketing.mindala_news_list", values)
        return response
