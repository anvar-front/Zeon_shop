# Generated by Django 4.0.4 on 2022-06-20 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='favorite',
        ),
    ]
