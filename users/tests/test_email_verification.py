from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from users.models import EmailVerification, User
import uuid
from datetime import timedelta
from django.utils.timezone import now
from model_bakery import baker


class EmailVerificationTestCase(TestCase):

    def setUp(self) -> None:
        self.user = baker.make(User, is_verified_email=False, email='mail@mail.com')
        self.record = EmailVerification.objects.create(code=uuid.uuid4(), user=self.user,
                                                       expiration=now() + timedelta(days=2))
        self.client.force_login(self.user)
        self.path = reverse('users:email_verification', kwargs={'email': self.user.email,
                                                                'code': self.record.code})

    def _common_test(self, response):
        self.assertTemplateUsed(response, 'users/email_verification.html')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_email_verification_success(self):
        self.assertFalse(self.user.is_verified_email)
        response = self.client.get(self.path)
        self._common_test(response)
        self.user.refresh_from_db()
        self.assertTrue(self.user.is_verified_email)
        self.assertContains(response, 'Ваша учетная запись успешно подтверждена!')

    def test_email_verification_expired_link(self):
        self.record.expiration = now()
        self.record.save()
        response = self.client.get(self.path)
        self._common_test(response)
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_verified_email)
        self.assertContains(response, 'Срок действия ссылки истек!')
