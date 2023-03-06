from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.models import User
from store_stepik.celery import app
from users.models import EmailVerification
from datetime import timedelta
from django.utils.timezone import now


class UserRegistrationViewTestCase(TestCase):

    def setUp(self) -> None:
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'alex', 'last_name': 'alex',
            'username': 'alex', 'email': 'alex@alex.com',
            'password1': "!QAZ@WSX", 'password2': '!QAZ@WSX'
        }

    app.conf.update(CELERY_ALWAYS_EAGER=True)

    def test_user_registration_get(self):
        response = self.client.get(self.path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/register.html')

    def test_user_registration_post_success(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        # check creating of user
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        # check creating of email verification
        email_verification = EmailVerification.objects.filter(user_id=User.objects.filter(username=username)[0].id)
        self.assertTrue(email_verification.exists())
        self.assertEqual(email_verification.first().expiration.date(),
                         (now() + timedelta(hours=48)).date()
                         )

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Пользователь с таким именем уже существует.', html=True)