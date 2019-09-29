from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


class HomePageTest(TestCase):

        # found = resolve('/') 
        # self.assertEqual(found.func, home_page)
    
    def test_uses_home_template(self):
        # 
        response = self.client.get('/')
        self.assertTemplateUsed(response,'home.html')

        # html = response.content.decode('utf8')
        # expected_html = render_to_string('home.html')
        # self.assertEqual(html, 
    # def test_root_url_resolves_to_home_page_view(seexpected_html)
    #     self.assertTrue(html.startswith('<html>'))
    #     self.assertIn('<title>To-Do lists</title>', html)
    #     self.assertTrue(html.strip().endswith('</html>'))
        
    #     self.assertTemplateUsed(response, 'home
    #     .html')