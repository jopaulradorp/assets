# -*- coding: utf-8 -*-
{
    'name': "Quantity based asset creation",
    'version': '16.0',
    'author': 'RADORP Pvt.Ltd',
    'summary': """
        Create assets for each purchased quantity.""",
    'description': """ Quantity based asset creation """,
    'website': "https://radorp.com/",
    'category': 'Accounting',
    'version': '10',
    'license': 'LGPL-3',
    'images': ['static/description/qty_based_assets.png'],
    'depends': ['om_account_asset', 'stock'],
    'data': [
        'views/account_asset.xml',
        'views/stock_lot.xml',
    ],
    'installable': True,
}
