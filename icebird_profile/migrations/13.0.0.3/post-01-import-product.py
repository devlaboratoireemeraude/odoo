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

        categ_ids = env['product.category'].search([('name', '=', 'Produits finis')])
        for product in env['product.template'].search([('type', '=', 'product'),('categ_id', 'in', categ_ids.ids)]):
            new_product = product.copy()
            product.barcode = None
            new_product = product.copy()
            product.barcode = None
            new_product.name = product.name
            new_product.default_code = product.default_code
            new_product.barcode = product.barcode
            try:
                product.action_archive()
            except:
                pass