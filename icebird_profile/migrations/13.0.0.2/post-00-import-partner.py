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

        logger.info('Import suppliers')

        with open(path.dirname(path.realpath(__file__)) + '/fournisseurs.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';', quotechar='"')
            column_names = next(reader)

            for row in reader:
                if row[column_names.index('nom')] and row[column_names.index('est une entreprise')]:
                    ResPartner = env['res.partner'].create({
                        'name': row[column_names.index('nom')],
                        'is_company': row[column_names.index('est une entreprise')],
                        'siret':row[column_names.index('siret')],
                        'street': row[column_names.index('rue')],
                        'zip': row[column_names.index('code postal')],
                        'city': row[column_names.index('ville')],
                        'vat': row[column_names.index('N° TVA')],
                        'phone':row[column_names.index('phone')],
                        'email': row[column_names.index('email')],
                        'ref':row[column_names.index('Code client')],
                        'internal_partner_code':row[column_names.index('code interne partenaire')],
                    })

                    if row[column_names.index('nom')] and row[column_names.index('est une entreprise')] and row[column_names.index('IBAN')]:
                        bank_exist = env['res.bank'].search([
                            ('name', '=',row[column_names.index('Nom de la banque')])
                        ])
                        if not bank_exist:
                            ResBank = env['res.bank'].create({
                                'name': row[column_names.index('Nom de la banque')],
                            })
                            partner = env['res.partner'].search([
                                ('is_company', '=', True),
                                ('name', '=', row[column_names.index('nom')]),
                            ])
                            if partner:
                                env['res.partner.bank'].create({
                                    'bank_id': ResBank.id,
                                    'partner_id': partner.id,
                                    'acc_number': row[column_names.index('IBAN')],
                                })
                                AccountPaymentTerm = env['account.payment.term'].create({
                                    'name': row[column_names.index('Conditions de paiement')]
                                })
                                partner.write({
                                    'property_payment_term_id': AccountPaymentTerm.id
                                })
                    if row[column_names.index('contact')]:
                        company = env['res.partner'].search([
                            ('name', '=', row[column_names.index('nom')],),
                            ('is_company', '=', True),
                        ],limit=1)
                        env['res.partner'].create({
                            'name':row[column_names.index('contact')],
                            'type': 'contact',
                            'function': row[column_names.index('poste occupé')],
                            'email':row[column_names.index('Email-child')],
                            'phone':row[column_names.index('téléphone')],
                            'parent_id':company.id
                        })
                    if row[column_names.index('tag')]:
                        partner = env['res.partner'].search([('name', '=', row[column_names.index('nom')]), ])
                        partner_tag_exist = env['res.partner.category'].search([
                            ('name', '=', row[column_names.index('tag')])
                        ])
                        if not partner_tag_exist:
                            Tag = env['res.partner.category'].create({
                                'name': row[column_names.index('tag')]
                            })
                        partner.write({
                            'category_id': [(6, 0, [partner_tag_exist.id or Tag.id])]
                        })