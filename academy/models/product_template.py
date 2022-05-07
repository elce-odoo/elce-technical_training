# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError

class ProductTemplate(models.Model):

    _inherit = 'product.template'

    is_session_product = fields.Boolean(string='Use as session product',
                                        default=False)
