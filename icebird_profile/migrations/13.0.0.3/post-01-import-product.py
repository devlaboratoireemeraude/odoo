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

        for product in env['product.template'].search([]):
            if product.default_code and not product.default_code[0:2] == 'PF':
                product_name = product.name
                new_product = product.copy(default={'name': product_name})
                product.barcode = None
                new_product.default_code = product.default_code
                new_product.barcode = product.barcode
                env.cr.commit()
                print(new_product.name)
                try:
                    product.action_archive()
                except:
                    pass