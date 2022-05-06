# -*- coding: utf-8 -*-


import string
from odoo import models, fields, api
# from odoo.exceptions import  UserError, ValidationError

class Mission(models.Model):
    
    _name = "moon.mission"
    _description = "Mission info"

    name = fields.Char(Char="Title")
    destination = fields.Char(string="Destination")
    active = fields.Boolean(string='Active', default=True)

    leader_id = fields.Many2one(comodel_name='res.partner', 
                            string='Leader')

    spaceship_id = fields.Many2one(comodel_name='moon.spaceship',
                                string='Spaceship',
                                ondelete='cascade',
                                required=True)

    # crew_ids = fields.Many2many(comodel_name='res.partner',
    #                             string='Crew')

    
