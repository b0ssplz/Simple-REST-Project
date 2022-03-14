from django.test import TestCase
from .models import Product

# Create your tests here.

class BasicTest(TestCase):
    def test_fields(self):
        product = Product()
        product.name = "test_product_name"
        product.amount_in_stock = 10
        product.save()
        
        record = Product.objects.get(pk=1)
        self.assertEqual(record,product)
        