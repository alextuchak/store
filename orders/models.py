from django.db import models
from users.models import User
from django.core.validators import RegexValidator


class Order(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен')
    )
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    cell_phone_regex = RegexValidator(regex=r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
    cell_phone = models.CharField(validators=[cell_phone_regex], unique=True, max_length=11, default='')
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict)
    created = models.DateField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order #{self.id}. {self.first_name} {self.last_name}'



