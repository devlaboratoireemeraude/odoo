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

        with open(path.dirname(path.realpath(__file__)) + '/categ.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            column_names = next(reader)
            for row in reader:
                if row[column_names.index('Parents')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('Parents')]),
                    ])
                    if not search_categ:
                        ParentCateg = env['product.category'].create({
                            'name':row[column_names.index('Parents')],
                            'parent_id': env.ref('product.product_category_1').id,
                        })
                if row[column_names.index('child1')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('child1')])
                    ])
                    if not search_categ:
                        Parent2Categ = env['product.category'].create({
                            'name':row[column_names.index('child1')],
                            'parent_id':ParentCateg.id
                        })
                if row[column_names.index('child2')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('child2')]),
                        ('parent_id', '=', Parent2Categ.id)
                    ])
                    if not search_categ:
                        Parent3Categ = env['product.category'].create({
                            'name':row[column_names.index('child2')],
                            'parent_id':Parent2Categ.id
                        })
                if row[column_names.index('child3')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('child3')]),
                        ('parent_id', '=', Parent3Categ.id)
                    ])
                    if not search_categ:
                        Parent4Categ = env['product.category'].create({
                            'name':row[column_names.index('child3')],
                            'parent_id':Parent3Categ.id
                        })
                if row[column_names.index('child4')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('child4')]),
                        ('parent_id', '=', Parent4Categ.id)
                    ])
                    if not search_categ:
                        Parent5Categ = env['product.category'].create({
                            'name':row[column_names.index('child4')],
                            'parent_id':Parent4Categ.id
                        })
                if row[column_names.index('child5')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('child5')]),
                        ('parent_id', '=', Parent5Categ.id)
                    ])
                    if not search_categ:
                        Parent6Categ = env['product.category'].create({
                            'name':row[column_names.index('child5')],
                            'parent_id':Parent5Categ.id
                        })
                if row[column_names.index('child6')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('child6')]),
                        ('parent_id', '=', Parent6Categ.id)
                    ])
                    if not search_categ:
                        Parent7Categ = env['product.category'].create({
                            'name':row[column_names.index('child6')],
                            'parent_id':Parent6Categ.id
                        })
                if row[column_names.index('child7')]:
                    search_categ = env['product.category'].search([
                        ('name', '=', row[column_names.index('child7')]),
                        ('parent_id', '=', Parent7Categ.id)
                    ])
                    if not search_categ:
                        Parent8Categ = env['product.category'].create({
                            'name':row[column_names.index('child7')],
                            'parent_id':Parent7Categ.id
                        })

