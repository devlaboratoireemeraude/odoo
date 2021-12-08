# -*- coding: utf-8 -*-
# Copyright 2021 CTO IT Consulting
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID
from odoo import api
import logging
logger = logging.getLogger()



def migrate(cr, v):

    with api.Environment.manage():
        uid = SUPERUSER_ID
        ctx = api.Environment(cr, uid, {})['res.users'].context_get()
        env = api.Environment(cr, uid, ctx)

        logger.info('Import products')

        for product in env['product.template'].search([('type', '=', 'product')]):
            new_product = product.copy()
            barcode = product.barcode
            product.barcode = None
            new_product.write({
                'name': product.name,
                'default_code': product.default_code,
                'barcode': barcode
            })
            try:
                product.action_archive()
            except:
                pass