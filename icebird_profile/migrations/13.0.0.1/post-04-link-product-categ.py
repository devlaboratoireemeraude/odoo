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
        self = env['res.users'].browse(2)

        logger.info('Import supplier')

        with open(path.dirname(path.realpath(__file__)) + '/inventaire.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            column_names = next(reader)
            vals = []
            column_names[0] = 'default_code'
            for row in reader:
                categories = env['product.category'].search([])
                for categ in categories:
                    categ.write({'name':categ.name.strip() })

                if row:
                    product_template = env['product.template'].search([
                        ('name', '=',row[column_names.index('Nom')] )
                    ])
                    if product_template:
                        list_catgories = row[column_names.index('Catégorie')].split('/')
                        product_category = env['product.category'].search([
                            ('name', '=', list_catgories[-1].strip()),
                            ('parent_id.name', '=', list_catgories[-2].strip())
                        ], limit=1)
                        if product_category:
                            product_template.write({
                                'categ_id': product_category.id
                            })
