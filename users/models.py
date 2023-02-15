from django.contrib.auth.models import AbstractUser
from django.core.mail import send_mail
from django.db import models
from django.urls import reverse
from django.utils.timezone import now

from store_stepik.settings import DOMAIN_NAME, EMAIL_HOST_USER


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)


class EmailVerification(models.Model):
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f'EmailVerification object for {self.user.email}'

    def send_verification_email(self):
        verification_link = f"{DOMAIN_NAME}" \
                        f"{reverse('users:email_verification', kwargs={'email': self.user.email,'code': self.code})}"
        subject = f"Подтверждение учетной записи для {self.user.username}"
        message = "Для подтверждения учетной записи для {} перейдите по ссылке: {}".format(
            self.user.email, verification_link)
        send_mail(
            subject=subject,
            message=message,
            from_email=EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False
        )

    def is_expired(self):
        return True if now() >= self.expiration else False

    class Meta:
        verbose_name = "Verification"
        verbose_name_plural = "Verifications"
