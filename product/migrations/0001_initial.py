# Generated by Django 4.0.4 on 2022-06-16 16:53

import ckeditor.fields
import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='collection/', verbose_name='Фотография')),
                ('title', models.CharField(max_length=255, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Коллекция',
                'verbose_name_plural': 'Коллекции',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('vendor_code', models.CharField(max_length=255, verbose_name='Артикул')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Скидка')),
                ('new_price', models.FloatField(blank=True, default=0, null=True, verbose_name='Цена после скидки')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Описание')),
                ('size_range', models.CharField(max_length=20, verbose_name='Размерный ряд')),
                ('fabric_structure', models.CharField(max_length=255, verbose_name='Состав ткани')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество')),
                ('material', models.CharField(max_length=255, verbose_name='Материал')),
                ('bestseller', models.BooleanField(default=False, verbose_name='Хит продаж')),
                ('new', models.BooleanField(default=True, verbose_name='Новый')),
                ('favorite', models.BooleanField(default=False, verbose_name='Избранный')),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.collection', verbose_name='Коллекция')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.CreateModel(
            name='Image_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='product/', verbose_name='Фотография')),
                ('color', colorfield.fields.ColorField(default='#fff', image_field=None, max_length=18, samples=None, verbose_name='Цвет')),
                ('image_color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product')),
            ],
        ),
    ]
