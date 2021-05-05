# -*- coding: utf-8 -*-
# Copyright 2021 Charles-Edouard Toutain
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import SUPERUSER_ID
from odoo import api
import csv
import logging
logger = logging.getLogger()
from os import path



def migrate(cr, v):

    with api.Environment.manage():
        uid = SUPERUSER_ID
        ctx = api.Environment(cr, uid, {})['res.users'].context_get()
        env = api.Environment(cr, uid, ctx)

        logger.info('Import supplier')

        with open(path.dirname(path.realpath(__file__)) + '/inventaire.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            column_names = next(reader)
            vals = []
            column_names[0] = 'default_code'
            for row in reader:
                if row and row[column_names.index('Fournisseur')] != '':
                    if row[column_names.index('Prix fournisseur')] != '':
                        supplier_price = float(row[column_names.index('Prix fournisseur')].replace(',', '.'))
                    else:
                        supplier_price = 0
                    if row[column_names.index('Qté Fournisseur')] == '':
                        row[column_names.index('Qté Fournisseur')] = 0
                    product_template_id = env['product.template'].search([
                        ('name', '=', row[column_names.index('Nom')])
                    ], limit=1).id
                    res_partner = env['res.partner'].search([
                        ('name', '=', row[column_names.index('Fournisseur')].strip())
                    ],limit=1)
                    if res_partner:
                        vals.append({
                            'name': res_partner.id,
                            'price': supplier_price,
                            'product_tmpl_id': product_template_id,
                            'min_qty': int(row[column_names.index('Qté Fournisseur')]),

                        })
            if vals:
                env['product.supplierinfo'].create(vals)