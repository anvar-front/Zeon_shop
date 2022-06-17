# Generated by Django 4.0.4 on 2022-06-16 16:53

import colorfield.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order_check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_line', models.IntegerField(verbose_name='Количество линеек')),
                ('quantity', models.IntegerField(verbose_name='Количество товара')),
                ('price', models.FloatField(verbose_name='Сумма')),
                ('discount', models.FloatField(verbose_name='Скидка')),
                ('final_price', models.FloatField(verbose_name='Итого к оплате')),
            ],
            options={
                'verbose_name': 'Чек',
                'verbose_name_plural': 'Чек',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True, verbose_name='Имя')),
                ('first_name', models.CharField(max_length=30, null=True, verbose_name='Фамилия')),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='Электронная почта')),
                ('phone_number', models.CharField(blank=True, default='+996(700)12-34-56', max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+996(700)12-34-56'.", regex='(\\+996)\\(\\d{3}\\)\\d{2}-\\d{2}-\\d{2}')], verbose_name='Номер телефона')),
                ('country', models.CharField(max_length=30, null=True, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, null=True, verbose_name='Город')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата оформления')),
                ('status', models.CharField(choices=[('new', 'Новый'), ('done', 'Оформлен'), ('denyed', 'Отменен')], default='new', max_length=30, verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'Заказы',
                'verbose_name_plural': 'Заказы',
            },
        ),
        migrations.CreateModel(
            name='Product_to_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('color', colorfield.fields.ColorField(default='#fff', image_field=None, max_length=18, samples=None, verbose_name='Цвет')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('size_range', models.CharField(max_length=20, verbose_name='Размерный ряд')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('new_price', models.FloatField(verbose_name='Цена после скидки')),
                ('quantity', models.IntegerField(verbose_name='Количество товара')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product', to='cart.order_check')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='order_check',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order', to='cart.orders'),
        ),
    ]
