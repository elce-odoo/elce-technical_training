# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleWizard(models.TransientModel):
    _name = 'moon.project.wizard'
    _description = 'Wizard: Quick '

    def _default_mission(self):
        return self.env['moon.mission'].browse(self._context.get('active_id'))
    
    mission_id = fields.Many2one(comodel_name='moon.mission',
                                 string='Mission',
                                 required=True,
                                 default=_default_mission)


    mission_crew_ids = Many2many(comodel_name='res.partner',
                                 string='Crew in mission',
                                 related='mission_id.crew_ids')

    crew_ids = Many2many(comodel_name='res.partner',
                         string='Crew for the project')

    def create_projects(self):
        mission_id = self.env['moon.mission'].search([('create_project', '=', True)], limit=1)
        if mission_id:
            for member in self.crew_ids:
                project_id = self.env['project.project'].create({
                    'company_id': self.env.company,
                    'name': 'sdf',
                    'alias_id': 'sdfd',
                })