from django.test import SimpleTestCase
from django.urls import reverse, resolve
from products.views import (all_products, product_detail,
                            add_product, edit_product,
                            delete_product, animal_products)


# Create your tests here
class TestProductsUrls(SimpleTestCase):
    """ Products app url tests """
    def test_all_products_url_is_resolved(self):
        """ all products list """
        url = reverse('products')
        self.assertEqual(resolve(url).func, all_products)

    def test_add_product_url_is_resolved(self):
        """ adding a product """
        url = reverse('add_product')
        self.assertEqual(resolve(url).func, add_product)

    def test_product_detail_url_is_resolved(self):
        """ product detail """
        product_id = 1
        url = reverse('product_detail', args=[product_id])
        self.assertEqual(resolve(url).func, product_detail)

    def test_animal_products_url_is_resolved(self):
        """ sort animal product """
        url = reverse('animal_products', args=['animal_choice'])
        self.assertEqual(resolve(url).func, animal_products)

    def test_edit_product_url_is_resolved(self):
        """ editing an product """
        product_id = 1
        url = reverse('edit_product', args=[product_id])
        self.assertEqual(resolve(url).func, edit_product)

    def test_delete_product_url_is_resolved(self):
        """ delete a product """
        product_id = 1
        url = reverse('delete_product', args=[product_id])
        self.assertEqual(resolve(url).func, delete_product)
