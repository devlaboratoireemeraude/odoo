# -*- coding: utf-8 -*-
# Copyright 2021 WEBEDOO
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    internal_partner_code = fields.Char('Internal Partner Code')
