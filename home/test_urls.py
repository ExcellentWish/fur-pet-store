from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import index, about, contact_us, privacy_policy, terms_conditions


class TestHomeUrls(SimpleTestCase):
    """ home app url tests """
    def test_home_url_is_resolved(self):
        """ index page """
        url = reverse('home')
        self.assertEqual(resolve(url).func, index)

    def test_about_url_is_resolved(self):
        """ about page """
        url = reverse('about')
        self.assertEqual(resolve(url).func, about)

    def test_contact_us_url_is_resolved(self):
        """ contact_us page """
        url = reverse('contact_us')
        self.assertEqual(resolve(url).func, contact_us)


    def test_terms_conditions_url_is_resolved(self):
        """ terms_conditions """
        url = reverse('terms_conditions')
        self.assertEqual(resolve(url).func, terms_conditions)

    
    def test_privacy_policy_url_is_resolved(self):
        """ privacy_policy page """
        url = reverse('privacy_policy')
        self.assertEqual(resolve(url).func, privacy_policy)
