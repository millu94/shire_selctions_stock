import unittest
from models.product import Product
from models.manufacturer import Manufacturer

class TestModels(unittest.TestCase):
    
    def setUp(self):
        self.manufacturer = Manufacturer("Push Print", "63 Townsend St, Glasgow", "Makes Stickers")
        self.product = Product("SS_Logo", "Stickers", 1000, 280.50, 1.00, 2)

    def test_product_has_name(self):
        self.assertEqual("SS_Logo", self.product.name)

    def test_product_has_description(self):
        self.assertEqual("Stickers", self.product.description)

    def test_product_has_quantity(self):
        self.assertEqual(1000, self.product.quantity)

    def test_product_has_buying_cost(self):
        self.assertEqual(280.50, self.product.buying_cost)
        
    def test_product_has_selling_price(self):
        self.assertEqual(1.00, self.product.selling_price)

    def test_product_has_manufacturer_id(self):
        self.assertEqual(2, self.product.manufacturer_id)

    def test_manufacturer_has_name(self):
        self.assertEqual("Push Print", self.manufacturer.name)

    def test_manufacturer_has_address(self):
        self.assertEqual("63 Townsend St, Glasgow", self.manufacturer.contact_details)

    def test_manufacturer_has_info(self):
        self.assertEqual("Makes Stickers", self.manufacturer.info)




