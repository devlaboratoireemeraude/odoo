# -*- coding: utf-8 -*-
# Copyright 2021 WEBEDOO
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    external_ref = fields.Char('External Ref')
