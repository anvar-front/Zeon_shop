# Generated by Django 4.0.4 on 2022-06-04 18:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_call_back_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='call_back',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+996700000000'. Up to 15 digits allowed.", regex='^/(\\+[996|7]\\()(\\d{3})(\\)\\d{2,3}-\\d{2}-\\d{2})/e$')]),
        ),
    ]
