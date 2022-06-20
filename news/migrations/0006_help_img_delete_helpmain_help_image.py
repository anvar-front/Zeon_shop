# Generated by Django 4.0.4 on 2022-06-01 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_remove_helpmain_questions_helpmain_questions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Help_img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='help/')),
            ],
        ),
        migrations.DeleteModel(
            name='HelpMain',
        ),
        migrations.AddField(
            model_name='help',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='news.help_img'),
        ),
    ]