from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
User = get_user_model()

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="securepassword", email="arjun.deka@gmail.com", role="student")

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse("custom_auth:login"), {'username': 'testuser', 'password': 'securepassword',})
        self.assertEqual(response.status_code, 302)  # Adjust based on your redirect or response

    def test_login_with_invalid_credentials(self):
        response = self.client.post('custom_auth:login', {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_register_page_redirects_logged_in_users(self):
        self.client.login(username="testuser", password="securepassword")
        response = self.client.get(reverse("custom_auth:register"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("main:home"))

    def test_login_page_redirects_logged_in_users(self):
        self.client.login(username="testuser", password="securepassword")
        response = self.client.get(reverse("custom_auth:login"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("main:home"))

