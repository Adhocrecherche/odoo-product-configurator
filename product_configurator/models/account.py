# -*- coding: utf-8 -*-

from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    product_id = fields.Many2one(domain=[('config_ok', '=', False)])
