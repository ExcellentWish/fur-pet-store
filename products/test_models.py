from django.test import TestCase
from .models import Product, Category


class TestProductsModels(TestCase):
    """ tests for the product model """
    def setUp(self):
        self.category1 = Category.objects.create(
            name='tin_food',
            friendly_name='Canned Food'
        )
        self.category2 = Category.objects.create(
            name='dry_food',
            friendly_name='Dry Food'
        )
        self.product1 = Product.objects.create(
            name='Test 1234',
            category=self.category1,
            quantity_in_stock=5,
            price=15.00,
        )

    def test_product_name(self):
        product = self.product1
        self.assertEqual(str(product), 'Test 1234')

    def test_stock_label_change(self):
        product = self.product1
        product.quantity_in_stock = 0
        self.assertEqual(product.in_stock, False)

    def test_category_name(self):
        category = self.category1
        self.assertEqual(str(category), 'tin_food')

    def test_category_name_to_display(self):
        category = self.category1
        friendly_name = category.get_friendly_name()
        self.assertEqual(friendly_name, 'Canned Food')
