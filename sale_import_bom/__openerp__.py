# -*- coding: utf-8 -*-

{
    'name': 'Import BOM in sale order lines',
    'version': '1.0',
    'category': 'Sales',
    'description': """
This module fills the sales order with bom
    """,
    'author': '3nodus',
    'website': 'http://www.3nodus.com',
    'depends': ['mrp','sale'],
    'data': [
        'sale_import_bom_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
