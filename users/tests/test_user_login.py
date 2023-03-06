from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.models import User


class TestUserLoginViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('users:login')
        self.data = {"username": "user", "password": "!QAZ@WSX"}
        self.user = User.objects.create(username=self.data["username"])
        self.user.set_password(self.data["password"])
        self.user.save()

    def test_login_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertEqual(response.context_data['title'], 'Store - Авторизация')

    def test_login_post_success(self):
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertTrue(self.user.is_authenticated)
        self.assertRedirects(response, reverse('index'))

    def test_login_post_error(self):
        self.data['username'] = 'user12'
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response,'Пожалуйста, введите правильные имя пользователя и пароль. '
                                     'Оба поля могут быть чувствительны к регистру.')

