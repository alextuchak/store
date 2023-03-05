from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
import uuid
from datetime import timedelta
from django.utils.timezone import now
from common.views import TitleMixin
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User
from store_stepik.settings import DOMAIN_NAME, EMAIL_HOST_USER


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Store - Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляем! Вы успешно зарегистрированы!'
    title = 'Store - Регистрация'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Store - Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        if not User.objects.get(username=context.get('user')).is_verified_email:
            context['messages'] = 'Для создания заказа необходимо подвердить email'
        if not User.objects.get(username=context.get('user')).email:
            context['no_email'] = 'Отсутствует email'
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - Подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
        return super(EmailVerificationView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(EmailVerificationView, self).get_context_data()
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and email_verifications.first().is_expired():
            context['expired'] = True
        return context


@login_required
def send_verification_email(request, *args, **kwargs):
    user = request.user
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
    return HttpResponseRedirect(reverse('index'))
