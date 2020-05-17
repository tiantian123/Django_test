from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.models import Item
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
from lists.views import home_page


class HomePageTest(TestCase):

    def test_root_url_resolve_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # @csrf_exempt
    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(), expected_html)

    # @csrf_exempt
    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html', {
            'new_item_text': 'A new list item'})
        self.assertEqual(response.content.decode(), expected_html)


class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        save_items = Item.objects.all()
        self.assertEqual(save_items.count(), 2)

        first_save_item = save_items[0]
        second_save_item = save_items[1]
        self.assertEqual(first_save_item.text, 'The first (ever) list item')
        self.assertEqual(second_save_item.text, 'Item the second')