from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestMainViews(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)


class TestAccountsViews(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.credentials = {
            'username': 'test_user',
            'password1': 'test_password1',
            'password2': 'test_password1',
        }

    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_signup_redirect(self):
        response = self.client.post(reverse('signup'), self.credentials)
        self.assertRedirects(response, reverse('home'))

    def test_signup_csrf(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'csrfmiddlewaretoken')



