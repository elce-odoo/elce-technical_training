# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):

    _name="academy.course"
    _description="Academy course"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    

    active = fields.Boolean(string='Active', default=True)

    base_price = fields.Float(string="Base Price", default = 0.0)

    additional_price = fields.Float(string="Additional Price", default=0.0)

    total_price = fields.Float(string="Total price", readonly=True)

    session_ids = fields.One2many(comodel_name="academy.session",
                                  inverse_name="course_id",
                                  string="Sessions")

    @api.onchange('base_price', 'additional_price')
    def _onchange_additional_price(self):
        if self.base_price < 0.00:
            raise UserError('Base price cannot be negative')

        self.total_price = self.base_price + self.additional_price