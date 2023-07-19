# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class Songs(http.Controller):
    @http.route('/canciones/<model("music.songs"):song>', auth="public", website=True,sitemap=True)
    def song(self, song):
        template = "music.single_song"
        if song.template :
            template = "music."+song.template
        return request.render(template, {'song':song} )
    
class Artists(http.Controller):
    @http.route('/artistas/<model("music.artists"):artist>', type='http', auth="public", website=True, sitemap=True)
    def song(self, artist=None):
        values = {"artist" : artist}
        return request.render("music.single_artist", values)