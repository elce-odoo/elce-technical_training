# -*- coding utf-8 -*-

from odoo import models, fields, api

class Project(models.Model):
    _inherit = 'project.project'

    mission_id = fields.Many2one(comodel_name='moon.mission',
                                 string='Related Mission',
                                 ondelete='set null')

    leader_id = fields.Many2one(string='Mission Instructor',
                                related='mission_id.leader_id')

    crew_ids = fields.Many2many(string='Crew',
                                related='mission_id.crew_ids')

    spaceship_id = fields.Many2one(string='Spaceship',
                                related='mission_id.spaceship_id')

