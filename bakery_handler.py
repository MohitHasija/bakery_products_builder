"""
This file implements the Bakery Handler class and methods that
are used to process the user input and finally provide the required
output.

"""


import os, sys, logging
from bakery_product import BakeryProduct, BakeryPackQuantityAndCost


bakery_products = [
  ('Vegemite Scroll', 'VS5', ('3 @ $6.99', '5 @ $8.99')),
  ('Blueburry Muffin', 'MB11', ('2 @ $9.95', '5 @ $16.95', '8 @ $24.95')),
  ('Croissant', 'CF', ('3 @ $5.95', '5 @ $9.95', '9 @ $16.99'))
]

class ProductsHandler(object):
    def __init__(self, bakery_products):

        self.bakery_products_code_map = {}
        for each_product in bakery_products:
            name = each_product[0]
            code = each_product[1]
            pack_quantity_and_cost_list = []
            for each_entry in each_product[2]:
                pack_quantity_and_cost_list.append(BakeryPackQuantityAndCost(each_entry.split(' ')[0],
                                                                             each_entry.split(' ')[-1]))
            self.bakery_products_code_map[code] = BakeryProduct(name, code, pack_quantity_and_cost_list)

    def get_map_bakery_products(self):
        return self.bakery_products_code_map

    def get_least_cost_of_product_packing(self, product_code, number_of_packs_ordered):
        bakery_product_object = self.bakery_products_code_map.get(product_code, None)
        if not bakery_product_object:
            return tuple()
        logging.info("Initiating process for product: {}".format(bakery_product_object.name))
        print("Initiating process for product: {}".format(bakery_product_object.name))
        return bakery_product_object.get_minimium_cost_of_packing(number_of_packs_ordered)
