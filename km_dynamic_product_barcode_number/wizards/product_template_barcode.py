from odoo import api, fields, models, _
from . import barcode


class DynamicProductBarcode(models.TransientModel):
    _name = 'dynamic.product.template.barcode.number'

    @api.model
    def default_get(self, fields):
        res = super(DynamicProductBarcode, self).default_get(fields)
        active_ids = self._context.get('active_ids')
        sale_order_ids = self.env['product.template'].browse(active_ids)
        print("default_get:", sale_order_ids)
        return res


    def dynamic_product_barcode(self):
        print('Confirm barcode generator')
        self.ensure_one()
        product_ids = self.env['product.template'].browse(self._context.get('active_ids'))

        for prod in product_ids:
            product_id = prod.id
            product_product_ids = self.env['product.product'].search([('product_tmpl_id','=',product_id)])
            print('product_product_id:',product_product_ids)
            for prod_prod_id in product_product_ids:
                print('prod_prod_id:',prod_prod_id)
                product_product_id = prod_prod_id.id
                eanbarcode = barcode.generate_ean(self, str(product_product_id))
                self.env.cr.execute(
                    "update product_product set barcode='" + str(eanbarcode) + "' where id='" + str(product_product_id) + "'")
