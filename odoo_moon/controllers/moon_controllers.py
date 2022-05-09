# -*- coding: utf-8 -*-

from odoo import http

class Moon(http.Controller):
    @http.route('/moon/', auth='public', website=True)
    def index(self, **kw):
        return "Hello world"
    
    @http.route('/moon/missions/', auth='public', website=True)
    def missions(self, **kw):
        missions = http.request.env['moon.mission'].search([])
        return http.request.render('odoo_moon.mission_website', {
            'missions': missions,
        })

    @http.route('/moon/<model("moon.spaceship"):spaceship>/', auth='public', website=True)
    def spaceship(self, spaceship):
        return http.request.render('odoo_moon.spaceship_website',{
            'spaceship': spaceship,
        })