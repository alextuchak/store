from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.models import EmailVerification, User
from model_bakery import baker
from store_stepik.celery import app


class UserEmailSendTestCase(TestCase):
    def setUp(self) -> None:
        self.user = baker.make(User, email='mail@mail.com')
        app.conf.update(CELERY_ALWAYS_EAGER=True)
        self.path = reverse('users:send_verification')
        self.client.force_login(self.user)

    def test_verification_email_send(self):
        self.assertFalse(EmailVerification.objects.filter(user_id=self.user.id).exists())
        response = self.client.get(self.path)
        self.assertTrue(EmailVerification.objects.filter(user_id=self.user.id).exists())
