# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class MindalaNews(http.Controller):
    @http.route(
        [
            """/noticias/<model("mindala.m4pnews"):m4pnews>""",
        ],
        type="http",
        auth="public",
        website=True,
        sitemap=True,
    )
    def m4pnews(self, m4pnews):
        values = {
            "m4pnews": m4pnews,
            "main_object": m4pnews,
        }
        response = request.render("mindala_news.m4pnews_complete", values)
        return response

    @http.route(
        ["""/noticias"""], type="http", auth="public", website=True, sitemap=True
    )
    def get_news(self, limit="15"):
        values = {}
        values["m4pnews"] = request.env["mindala.m4pnews"].search([])
        response = request.render("mindala_news.m4pnews_list", values)
        return response
