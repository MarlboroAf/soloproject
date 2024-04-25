from django.test import Client, TestCase
from django.urls import reverse
from django.utils import timezone
from shop.models import Product
from shop.forms import ProductForm


# Create your tests here.

class ShopFormTests(TestCase):
        @classmethod
        def setUpTestData(cls):
            Product.objects.create(name = "Acme Toaster", price= 23.99)
            Product.objects.create(name = "Acme Stool", price= 3.99)
            

        def test_product_new(self):
            form = ProductForm(data={"name": "my gadget", "price": 3.45})
            self.assertTrue(form.is_valid())
            product = form.save(commit=False)
            product.created_date = timezone.now()
            product.save()
            self.assertEqual(product.name, 'my gadget')
           
        # add edit test using the form
  