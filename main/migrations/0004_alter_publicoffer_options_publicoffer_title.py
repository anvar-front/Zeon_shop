# Generated by Django 4.0.4 on 2022-06-01 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_publicoffer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicoffer',
            options={'verbose_name': 'Публичная оферта', 'verbose_name_plural': 'Публичная оферта'},
        ),
        migrations.AddField(
            model_name='publicoffer',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
