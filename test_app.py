# NexaShop Unit Tests
import unittest
from app import get_product, calculate_total

class TestNexaShop(unittest.TestCase):
    
    def test_get_existing_product(self):
        """Test retrieving an existing product"""
        product = get_product(1)
        self.assertIsNotNone(product)
        self.assertEqual(product["name"], "Laptop")
        self.assertEqual(product["price"], 999.99)
    
    def test_get_nonexistent_product(self):
        """Test retrieving a product that doesn't exist"""
        product = get_product(99)
        self.assertIsNone(product)
    
    def test_calculate_total(self):
        """Test order total calculation"""
        items = [
            {"name": "Laptop", "price": 999.99},
            {"name": "Phone", "price": 499.99}
        ]
        total = calculate_total(items)
        self.assertEqual(total, 1499.98)

if __name__ == "__main__":
    unittest.main()
