from django.test import TestCase, Client
from .models import Product

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        self.product = Product.objects.create(
            name = "Item test",
            amount = 10,
            description = "Description test",
            power = 10,
            mana = 10,
            categories = "Category test",
        )

    def test_product_is_assign(self):
        product = Product.objects.get(id=self.product.id)
        self.assertEqual(product.name, "Item test")
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.description, "Description test")
        self.assertEqual(product.power, 10)
        self.assertEqual(product.mana, 10)
        self.assertEqual(product.categories, "Category test")