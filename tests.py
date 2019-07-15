"""
This file is usedt o run the tests on various methods and classes
written for Bakery Products Handler.

"""

import unittest
from bakery_handler import ProductsHandler, bakery_products


def initialise_bakery_products():
    return ProductsHandler(bakery_products)


class TestBakeryProductsInitialise(unittest.TestCase):
    def setUp(self):
        self.products_handler = initialise_bakery_products()

    def test_initialise(self):
        assert self.products_handler.get_map_bakery_products()['VS5'].name == 'Vegemite Scroll'

    def test_10_VS5(self):
        minimium_cost, tuple_with_minimium_cost = self.products_handler.get_least_cost_of_product_packing('VS5', 10)
        assert tuple_with_minimium_cost == (5,5)
        assert minimium_cost == 17.98

    def test_14_MB11(self):
        minimium_cost, tuple_with_minimium_cost = self.products_handler.get_least_cost_of_product_packing('MB11', 14)
        print(minimium_cost, tuple_with_minimium_cost)
        assert tuple_with_minimium_cost == (2, 2, 2, 8)
        assert minimium_cost == 54.8

    def test_13_CF(self):
        minimium_cost, tuple_with_minimium_cost = self.products_handler.get_least_cost_of_product_packing('CF', 13)
        print(minimium_cost, tuple_with_minimium_cost)
        assert tuple_with_minimium_cost == (3, 5, 5)
        assert minimium_cost == 25.85




if __name__=='__main__':
    unittest.main()