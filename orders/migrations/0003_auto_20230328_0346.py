# Generated by Django 3.2.13 on 2023-03-28 03:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='email',
            new_name='initiator',
        ),
        migrations.AddField(
            model_name='order',
            name='cell_phone',
            field=models.CharField(default='', max_length=11, unique=True, validators=[django.core.validators.RegexValidator(regex='^((8|\\+7)[\\- ]?)?(\\(?\\d{3}\\)?[\\- ]?)?[\\d\\- ]{7,10}$')]),
        ),
    ]
