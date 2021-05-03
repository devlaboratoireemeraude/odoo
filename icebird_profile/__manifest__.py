# -*- coding: utf-8 -*-
{
    'name': "icebird_profile",

    'summary': """
        The module allows the customization of Odoo according to the specific needs of the client""",

    'description': """
        Developed by Charles-Edouard Toutain, company Webedoo, 
        this module was developed for the company Icebird Digital, 
        it allows you to customize odoo by overriding the methods.
    """,

    'author': "Toutain Charles-Edouard",
    'website': "https://www.webedoo.fr",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Customize',
    'version': '13.0.0.2',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','contacts', 'stock', 'purchase'],

    'data': [
        'views/res_partner.xml',
        'views/product_template.xml',
    ],


}
