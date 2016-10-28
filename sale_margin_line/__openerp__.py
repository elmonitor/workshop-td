{
    'name': 'Margins in Sales Order lines',
    'version':'1.0',
    'category' : 'Sales Management',
    'description': """
This module adds the 'Margin' on sales order lines.
=============================================

This gives the profitability by calculating the price unit with the division between the purchase price and the margin factor.
Price and Cost Price.
    """,
    'author':'3nodus',
    'depends':['sale'],
    'demo':[],
    'test': [],
    'data':['sale_line_margin_view.xml'],
    'auto_install': False,
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

