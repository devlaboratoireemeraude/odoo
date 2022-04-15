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
                new_categories = env['product.category'].search([])
                # if row and row[column_names.index('Catégorie')] != '':
                #     for new_categ in new_categories:
                #         path_category = row[column_names.index('Catégorie')].strip()                      
                #         search_anomalie = env['product.category'].search([]).filtered(lambda c: c.display_name == path_category)
                #         if not search_anomalie:
                #             import pdb; pdb.set_trace()
                if row:
                    product_template = env['product.template'].search([
                        ('name', '=',row[column_names.index('Nom')] )
                    ])
                    if product_template:
                        print(row[column_names.index('default_code')])
                        list_catgories = row[column_names.index('Catégorie')].split('/')
                        print(list_catgories)
                        if len(list_catgories) == 1:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                            ])
                        if len(list_catgories) == 2:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()), 
                            ])
                        if len(list_catgories) == 3:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()), 
                                ('parent_id.parent_id.name', '=', list_catgories[-3].strip()),
                            ])
                        if len(list_catgories) == 4:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()), 
                                ('parent_id.parent_id.name', '=', list_catgories[-3].strip()),
                                ('parent_id.parent_id.parent_id.name', '=', list_catgories[-4].strip()),
                            ])
                        if len(list_catgories) == 5:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()), 
                                ('parent_id.parent_id.name', '=', list_catgories[-3].strip()),
                                ('parent_id.parent_id.parent_id.name', '=', list_catgories[-4].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-5].strip()),
                            ])
                        if len(list_catgories) == 6:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()), 
                                ('parent_id.parent_id.name', '=', list_catgories[-3].strip()),
                                ('parent_id.parent_id.parent_id.name', '=', list_catgories[-4].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-5].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-6].strip()),
                            ])
                        if len(list_catgories) == 7:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()),
                                ('parent_id.parent_id.name', '=', list_catgories[-3].strip()),
                                ('parent_id.parent_id.parent_id.name', '=', list_catgories[-4].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-5].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-6].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-7].strip()),
                            ])
                        if len(list_catgories) == 8:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()),
                                ('parent_id.parent_id.name', '=', list_catgories[-3].strip()),
                                ('parent_id.parent_id.parent_id.name', '=', list_catgories[-4].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-5].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-6].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-7].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-8].strip()),
                            ])
                        if len(list_catgories) == 9:
                            product_category = env['product.category'].search([
                                ('name', '=', list_catgories[-1].strip()),
                                ('parent_id.name', '=', list_catgories[-2].strip()),
                                ('parent_id.parent_id.name', '=', list_catgories[-3].strip()),
                                ('parent_id.parent_id.parent_id.name', '=', list_catgories[-4].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-5].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-6].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-7].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-8].strip()),
                                ('parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.parent_id.name', '=', list_catgories[-9].strip()),
                            ])
                        if product_category:
                            product_template.write({
                                'categ_id': product_category.id
                            })