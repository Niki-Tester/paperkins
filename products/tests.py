from django.test import TestCase
from .models import Product


class TestProductsApp(TestCase):
    """
    Test Products app
    """

    def setUp(self):
        Product.objects.create(
            name='Test Product',
            description='Test Description',
            price=2.99,
            stock_qty=12,
            active=True
        )

    def test_products_page(self):
        "Test products page renders correct page"
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_details_page(self):
        "Test products page renders correct page"
        product = Product.objects.first()
        response = self.client.get(f'/products/{product.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_details.html')
