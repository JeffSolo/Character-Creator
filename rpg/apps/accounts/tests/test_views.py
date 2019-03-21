from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class ClientTestCase(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()

    def check_status_code_200(self, viewname):
        url = reverse(viewname)
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def check_csrf(self, viewname):
        response = self.client.get(reverse(viewname))
        self.assertContains(response, 'csrfmiddlewaretoken')


class TestMainViews(ClientTestCase):
    def test_homepage_status_code(self):
        self.check_status_code_200('home')
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'csrfmiddlewaretoken')


class TestAccountsViews(ClientTestCase):
    @classmethod
    def setUp(cls):
        cls.credentials = {
            'username': 'test_user',
            'password1': 'test_password1',
            'password2': 'test_password1',
        }

    def test_signup_status_code(self):
        self.check_status_code_200('signup')

    def test_signup_redirect(self):
        response = self.client.post(reverse('signup'), self.credentials)
        self.assertRedirects(response, reverse('home'))

    def test_signup_csrf(self):
        self.check_csrf('signup')

    def test_login_status_code(self):
        self.check_status_code_200('login')

    def test_login_csrf(self):
        self.check_csrf('login')
