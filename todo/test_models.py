from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        item = Item.objects.create(name= 'Test todo Item')
        self.assertFalse(item.done)


    def test_item_string_mothod_returns_name(self):
        item = Item.objects.create(name= 'Test todo Item')
        self.assertEqual(str(item), 'Test todo Item')