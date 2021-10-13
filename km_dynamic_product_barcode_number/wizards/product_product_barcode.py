from odoo import api, fields, models, _
from . import barcode


class DynamicProductBarcode(models.TransientModel):
    _name = 'dynamic.product.product.barcode.number'

    @api.model
    def default_get(self, fields):
        res = super(DynamicProductBarcode, self).default_get(fields)
        active_ids = self._context.get('active_ids')
        sale_order_ids = self.env['product.product'].browse(active_ids)
        print("default_get:", sale_order_ids)
        return res

    def dynamic_product_barcode(self):
        print('Confirm barcode generator')
        self.ensure_one()
        product_ids = self.env['product.product'].browse(self._context.get('active_ids'))

        for prod in product_ids:
            product_id = prod.id
            print(product_id)
            eanbarcode = barcode.generate_ean(self, str(product_id))
            print('eanbarcode:',eanbarcode, "//product_id:",product_id)
            self.env.cr.execute(
                "update product_product set barcode='" + str(eanbarcode) + "' where id='" + str(product_id) + "'")
