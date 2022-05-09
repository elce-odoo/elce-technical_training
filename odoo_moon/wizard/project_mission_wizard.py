# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProjectWizard(models.TransientModel):
    _name = 'moon.project.wizard'
    _description = 'Wizard: Quick '

    def _default_mission(self):
        return self.env['moon.mission'].browse(self._context.get('active_id'))

    mission_id = fields.Many2one(comodel_name='moon.mission',
                                 string='Mission',
                                 required=True,
                                 default=_default_mission)

    mission_crew_ids = fields.Many2many(comodel_name='res.partner',
                                        string='Crew in mission',
                                        related='mission_id.crew_ids')

    crew_ids = fields.Many2many(comodel_name='res.partner',
                                string='Crew for the project')

    def create_projects(self):
        mission_id = self.env['moon.mission'].search(
            [('create_project', '=', True)], limit=1)
        if mission_id:
            project_id = self.env['project.project'].create({
                'company_id': self.env.company.id,
                'name': mission_id.name,
                'user_id': self.env.uid
                # 'alias_contact': '',
                # 'alias_defaults':'{}', test
                # 'alias_id': '',
                # 'alias_model_id': '',
                # 'privacy_visibility': '',
                # 'rating_status': '',
                # 'rating_status_period': ''
            })
