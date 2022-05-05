# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import  UserError, ValidationError

class Spaceship(models.Model):
    
    _name = "moon.spaceship"
    _description = "Spaceship info"


    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    owner = fields.Char(string='Title')
    state = fields.Selection(string='State')

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

    @api.onchange('description')
    def _check_description_length(self):
        for record in self:
            if len(record.description) > 10:
                raise ValidationError('too long')
