# Generated by Django 4.0.4 on 2022-06-04 18:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_call_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_back',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+996700000000'. Up to 15 digits allowed.", regex='^((8|\\+7|\\+996)[\\- ]?)?\\(?\\d{3,5}\\)?[\\- ]?\\d{1}[\\- ]?\\d{1}[\\- ]?\\d{1}[\\- ]?\\d{1}[\\- ]?\\d{1}(([\\- ]?\\d{1})?[\\- ]?\\d{1})?$')]),
        ),
    ]