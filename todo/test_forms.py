from django.test import TestCase
from .forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    

    def test_done_field(self):
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())
    

    def test_field_are_explicit(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])