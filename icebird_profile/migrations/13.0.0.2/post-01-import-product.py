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
                if row:
                    if row[column_names.index('Coût')] != '':
                        standard_price = float(row[column_names.index('Coût')].replace(',', '.'))
                    else:
                        standard_price = 0
                    if row[column_names.index('volume')] != '':
                        nb =  re.findall('\d+', row[column_names.index('volume')])[0];
                        volume = int(nb) / 1000
                    else:
                        volume = 0 
                    vals.append({
                        'default_code':row[column_names.index('default_code')],
                        'name':row[column_names.index('Nom')],
                        'purchase_ok': True,
                        'sale_ok': False,
                        'type': 'product',
                        'standard_price':standard_price,
                        'external_ref':row[column_names.index('Référence externe')],
                        'volume':volume,
                    })
            if vals:
                env['product.template'].create(vals)
            product_empty = env['product.template'].search([('name', '=', '')]).unlink()