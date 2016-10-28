

{
    'name' : 'Sale order hide elements',
    'version' : '1.0',
    'author' : '3nodus',
    'description': """
        This module customizes default view on sale order
    """,
    'category': 'Sales Management',
    'website' : 'www.3nodus.com',
    'depends' : ['sale','account','purchase'],
    'demo' : [],
    'data' : [
            'views/sale_view.xml',
            ],
    'test' : [],
    'auto_install': False,
    'application': True,
    'installable': True,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
