# -*- coding: utf-8 -*-

from openerp import fields, models, api

class ImportBom(models.Model):
    _inherit = "sale.order"
    bom_id = fields.Many2one('mrp.bom', string="Importar BOM", store=False)
    
    @api.multi
    def import_bom(self):
        print "***************************************************"

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
