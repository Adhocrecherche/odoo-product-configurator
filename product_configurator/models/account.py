# -*- coding: utf-8 -*-

from odoo import models, fields


# TODO V13: now account.move.line
class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    product_id = fields.Many2one(domain=[('config_ok', '=', False)])
