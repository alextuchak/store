from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.models import User


class UserLogoutTestCase(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(username='user', password='!QAZ@WSX')
        self.path = reverse('users:logout')

    def test_user_logout(self):
        self.client.force_login(self.user)
        response = self.client.post(self.path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('index'))




