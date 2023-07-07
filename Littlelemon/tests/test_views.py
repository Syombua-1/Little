#TestCase class
from restaurant.models import *
from django.test import TestCase
from restaurant.views import *

class MenuViewTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")