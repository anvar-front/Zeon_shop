# Generated by Django 4.0.4 on 2022-06-23 11:46

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image_color',
            name='color',
            field=colorfield.fields.ColorField(default='#fff', image_field=None, max_length=18, samples=None, verbose_name='Цвет'),
        ),
    ]
