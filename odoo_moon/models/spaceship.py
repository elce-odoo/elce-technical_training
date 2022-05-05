# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import  UserError, ValidationError

class Spaceship(models.Model):
    
    _name = "moon.spaceship"
    _description = "Spaceship info"


    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    # level = fields.Selection(string='Level',
    #                         selection=[('beginner', 'Beginner'),
    #                                    ('intermediate', 'Intermediate'),
    #                                    ('advanced', 'Advanced')],
    #                         copy=False)
    
    active = fields.Boolean(string='Active', default=True)

    height = fields.Float(string='Height')
    width = fields.Float(string='Width')

    crew_size = fields.Integer(string='Crew size')

    @api.constrains('width', 'height')
    def _check_measures(self):
        if self.width > self.height:
            raise UserError('Width cant be bigger than height')

    @api.constrains('description')
    def _check_description_length(self):
        if len(self.description) > 10:
            raise ValidationError('Too long dude')
