from django.test import TestCase


class TestProductsApp(TestCase):
    """
    Test Products app
    """

    def test_products_page(self):
        "Test products page renders correct page"
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
