from openerp import fields, api, models
import openerp.addons.decimal_precision as dp

class sale_order_line(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('margin_line')
    def _price_unit(self, cr, uid, ids, field_name, arg, context=None):
#        for line in self.browse(cr, uid, ids, context=context):
#            line.price_unit = line.purchase_price/(line.margin or 1.0)
        price = line.purchase_price/(line.margin or 1.0)
        res['value'].update({'price_unit': price})
    return res
