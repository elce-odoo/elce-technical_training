# -*- coding: utf-8 -*-

from odoo import models, fields

class Session(models.Model):

    _name="academy.course"
    _description="Academy course"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    
    active = fields.Boolean(string='Active', default=True)

    course_id = fields.Many2one(comodel_name='academy.course',
                                string='Course',
                                ondelete="cascade",
                                required=True)
    
    instructor_id = fields.Many2one(comodel_name='res.partner', string="Instructor")

    sudent_ids = fields.Many2many(comodel_name='res.partner', string="Students")