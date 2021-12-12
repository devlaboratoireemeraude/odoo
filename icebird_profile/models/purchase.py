# -*- coding: utf-8 -*-

from odoo import models, fields

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    user_id = fields.Many2one(required=True)
    incoterm_id = fields.Many2one(required=True)
    payment_term_id = fields.Many2one(required=True)
    fiscal_position_id = fields.Many2one(required=True)
    date_planned = fields.Datetime(required=True)