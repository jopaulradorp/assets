# -*- coding: utf-8 -*-
{
    'name': "Search transfers with Lot or Serial number",
    'version': '16.0',
    'author': 'RADORP Pvt.Ltd',
    'summary': """
        Search transfers using Lot/Serial Number.""",
    'description': """ Search transfers using Lot/Serial Number. """,
    'website': "https://radorp.com/",
    'category': 'Inventory',
    'version': '10',
    'license': 'LGPL-3',
    'images': ['static/description/banner.png'],
    'depends': ['stock'],
    'data': [
        'views/stock_picking.xml',
    ],
    'installable': True,
}
