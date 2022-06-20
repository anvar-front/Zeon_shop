# Generated by Django 4.0.4 on 2022-06-01 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_remove_helpmain_questions_helpmain_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpmain',
            name='questions',
        ),
        migrations.AddField(
            model_name='helpmain',
            name='questions',
            field=models.ManyToManyField(to='news.help'),
        ),
    ]