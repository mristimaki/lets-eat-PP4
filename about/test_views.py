from django.test import TestCase
from django.shortcuts import reverse


class TestAboutPage(TestCase):

    def test_get_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
