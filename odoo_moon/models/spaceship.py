# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import  UserError, ValidationError

class Spaceship(models.Model):
    
    _name = "moon.spaceship"
    _description = "Spaceship info"


    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')
    owner = fields.Text(string='Owner')
    state = fields.Selection(string='State', selection=[('draft', 'Draft'),
                                                        ('sold', 'Sold')])

    # level = fields.Selection(string='Level',
    #                         selection=[('beginner', 'Beginner'),
    #                                    ('intermediate', 'Intermediate'),
    #                                    ('advanced', 'Advanced')],
    #                         copy=False)
    
    active = fields.Boolean(string='Active', default=True)

    height = fields.Float(string='Height')
    width = fields.Float(string='Width')
    depth = fields.Float(string='Depth')

    volume = fields.Float(compute="_compute_volume", readonly=True)

    crew_size = fields.Integer(string='Crew size')

    crew_ids = fields.Many2many(string='Crew',
                                comodel_name="res.partner",
                                inverse_name="spaceship_id")

    missions = fields.One2many(string="Missions",
                                comodel_name="moon.mission",
                                inverse_name="spaceship_id")

    @api.depends('height', 'width', 'depth')
    def _compute_volume(self):
        for record in self:
            if not record.width or not record.height or not record.depth:
                record.volume = 0
            else:
                record.volume = record.width * record.height * record.depth


    @api.constrains('width', 'height')
    def _check_measures(self):
        if self.width > self.height:
            raise UserError('Width cant be bigger than height')

    @api.onchange('description')
    def _check_description_length(self):
        for record in self:
            if len(record.description) > 10:
                raise ValidationError('too long')

    @api.onchange('owner')
    def _update_state(self):
        for record in self:
            if len(record.owner) > 0:
                record.state = 'sold'
            else:
                record.state = 'draft' 

