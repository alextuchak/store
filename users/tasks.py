from celery import shared_task
from django.core.mail import send_mail

from users.models import User, EmailVerification
import uuid
from datetime import timedelta
from django.utils.timezone import now
from store_stepik.settings import DOMAIN_NAME, EMAIL_HOST_USER
from django.urls import reverse


@shared_task
def send_email_verification(user_id):
    user = User.objects.get(id=user_id)
    record = EmailVerification.objects.create(code=uuid.uuid4(), user=user, expiration=now() + timedelta(days=2))
    verification_link = f"{DOMAIN_NAME}" \
                        f"{reverse('users:email_verification', kwargs={'email': user.email, 'code': record.code})}"
    subject = f"Подтверждение учетной записи для {user.username}"
    message = "Для подтверждения учетной записи для {} перейдите по ссылке: {}".format(
        user.email, verification_link)
    send_mail(
        subject=subject,
        message=message,
        from_email=EMAIL_HOST_USER,
        recipient_list=[user.email],
        fail_silently=False
    )
