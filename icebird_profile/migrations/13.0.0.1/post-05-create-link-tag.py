# -*- coding: utf-8 -*-
# Copyright 2021 Charles-Edouard Toutain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID
from odoo import api
import csv
import logging
logger = logging.getLogger()
from os import path
import re



def migrate(cr, v):

    with api.Environment.manage():
        uid = SUPERUSER_ID
        ctx = api.Environment(cr, uid, {})['res.users'].context_get()
        env = api.Environment(cr, uid, ctx)

        logger.info('Import products')

        with open(path.dirname(path.realpath(__file__)) + '/inventaire.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            column_names = next(reader)
            vals = []
            supplier_vals = []
            column_names[0] = 'default_code'
            for row in reader:
                if row and row[column_names.index('tag')] != '':
                    product_template = env['product.template'].search([
                        ('name', '=', row[column_names.index('Nom')])
                    ])
                    product_tag = env['product.tags'].search([
                        ('name', '=', row[column_names.index('tag')])
                    ])
                    if not product_tag:
                        product_tag = env['product.tags'].create({
                            'name': row[column_names.index('tag')]
                        })
                    product_template.write({'tag_ids': [(4, product_tag.id)] })
