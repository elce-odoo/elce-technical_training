# -*- coding: utf-8 -*-

from odoo import models, fields

class SalesOrder(models.Model):

    _inherit="sales.order"

    session_id = fields.Many2one(comodel_name="academy.session",
                                string="Session",
                                ondelete="set null")


    instructor_id = fields.Many2one(string="Instructor",
                                    related="session_id.instructor_id")

    students_id = fields.Many2many(string="Students",
                                    related="session_id.students_ids")