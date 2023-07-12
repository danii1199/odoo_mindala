# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Songs(http.Controller):
    @http.route('/canciones/<model("music.songs"):song>', type='http', auth="public", website=True, sitemap=False)
    def song(self, song=None):
        values = {
            "song" : song
        }
        return request.render("music.single_song", values)
    
class Artists(http.Controller):
    @http.route('/artistas/<model("music.artists"):artist>', type='http', auth="public", website=True, sitemap=False)
    def song(self, artist=None):
        values = {"artist" : artist}
        return request.render("music.single_artist", values)