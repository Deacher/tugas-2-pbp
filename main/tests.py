from django.test import TestCase, Client
from .models import Item

class mainTest(TestCase):
    # def test_main_url_is_exist(self):
    #     response = Client().get('/main/')
    #     self.assertEqual(response.status_code, 200)

    # def test_main_using_main_template(self):
    #     response = Client().get('/main/')
    #     self.assertTemplateUsed(response, 'main.html')
    
    def setUp(self):
        self.item = Item.objects.create(
            name = "Item test",
            amount = 10,
            description = "Description test",
            power = 10,
            mana = 10,
            categories = "Category test",
        )

    def test_product_is_assign(self):
        item = Item.objects.get(id=self.item.id)
        self.assertEqual(item.name, "Item test")
        self.assertEqual(item.amount, 10)
        self.assertEqual(item.description, "Description test")
        self.assertEqual(item.power, 10)
        self.assertEqual(item.mana, 10)
        self.assertEqual(item.categories, "Category test")