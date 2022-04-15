# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2015 DevIntelle Consulting Service Pvt.Ltd (<http://www.devintellecs.com>).
#
#    For Module Support : devintelle@gmail.com  or Skype : devintelle
#
##############################################################################

{
    'name': 'Product Tags',
    'version': '13.0.1.0',
    'sequence': 1,
    'category': 'Generic Modules/Sales Management',
    'description':
        """
        This Module add below functionality into odoo

        1.This module will help to add tags in product\n

    """,
    'summary': 'odoo App will Add tags into product Screen',
    'author': 'DevIntelle Consulting Service Pvt.Ltd',
    'website': 'http://www.devintellecs.com',
    'depends': ['product'],
    'data': [
        'security/tags_security.xml',
        'security/ir.model.access.csv',
        'views/product_template.xml'
        ],
    'demo': [],
    'test': [],
    'css': [],
    'qweb': [],
    'js': [],
    'images': ['images/main_screenshot.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
