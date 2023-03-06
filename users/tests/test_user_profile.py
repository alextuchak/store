from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.models import User
from store_stepik.celery import app
from users.models import EmailVerification


class UserProfileTestCase(TestCase):

    def setUp(self) -> None:
        self.data = {"username": "user", 'email': "a@g.com",
                     "first_name": "user11", "last_name": "user1qa", 'image': ''}
        self.user = User.objects.create(username=self.data["username"], email=self.data['email'],
                                        is_verified_email=True, first_name=self.data['first_name'],
                                        last_name=self.data['last_name'])
        self.user.set_password("!QAZ@WSX")
        self.user.save()
        self.path = reverse('users:profile', kwargs={'pk': self.user.id})
        app.conf.update(CELERY_ALWAYS_EAGER=True)
        self.client.force_login(self.user)

    def _common_test(self, response):
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/profile.html')
        self.assertEqual(response.context_data['title'], 'Store - Личный кабинет')
        self.assertEqual(response.context_data['user'], self.user)

    def test_profile_get_success(self):
        response = self.client.get(self.path)
        self._common_test(response)

    def test_profile_get_error(self):
        self.client.logout()
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login') + '?next=' + self.path)

    def test_profile_get_without_email(self):
        self.user.email = ""
        self.user.save()
        response = self.client.get(self.path)
        self._common_test(response)
        self.assertEqual(response.context_data['no_email'], "Отсутствует email")

    def test_profile_get_unverified_email(self):
        self.user.is_verified_email = False
        self.user.save()
        response = self.client.get(self.path)
        self._common_test(response)
        self.assertEqual(response.context_data['messages'], 'Для создания заказа необходимо подвердить email')

    def test_profile_post_info(self):
        response = self.client.post(self.path, {"username": "user", 'email': "a@g.com",
                                                "first_name": "first", "last_name": "last", 'image': ''})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.user.refresh_from_db()
        self.assertEqual(self.user.last_name, 'last')
        self.assertEqual(self.user.first_name, 'first')

    def test_profile_post_email(self):
        self.user.email = ''
        self.user.is_verified_email = False
        self.user.save()
        self.assertFalse(EmailVerification.objects.filter(user_id=self.user.id).exists())
        self.assertFalse(self.user.email)
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, self.data['email'])
        self.assertTrue(EmailVerification.objects.filter(user_id=self.user.id).exists())

