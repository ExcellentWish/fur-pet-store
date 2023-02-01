from django.test import TestCase, Client
from django.urls import reverse


class TestHomeViews(TestCase):
    """ home app view tests """
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('home')
        self.contact_us_url = reverse('contact_us')
        self.privacy_policy_url = reverse('privacy_policy')
        self.terms_conditions_url = reverse('terms_conditions')
        self.about_url = reverse('about')

    def test_home_GET(self):
        """ get home view """
        response = self.client.get(self.index_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_contact_page_GET(self):
        """ get contact_us page view """
        response = self.client.get(self.contact_us_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/contact_us.html')

    def test_privacy_page_GET(self):
        """ get privacy page view """
        response = self.client.get(self.privacy_policy_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/privacy_policy.html')

    def test_about_page_GET(self):
        """ get about page view """
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about.html')

    def test_terms_page_GET(self):
        """ get terms_conditions page view """
        response = self.client.get(self.terms_conditions_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/terms_conditions.html')
