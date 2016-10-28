from openerp import fields, api, models
import openerp.addons.decimal_precision as dp

class sale_order_line(models.Model):
    _inherit = "sale.order.line"
    margin_line=fields.Float('Margen')
    @api.multi
    @api.onchange('margin_line','purchase_price')
    def _price_unit(self):
        price = self.purchase_price/((1-self.margin_line/100) or 1.0)
        price =round(price,0)
        self.price_unit = price        
