from django.db import models
from colorfield.fields import ColorField
from user.models import User

from django.core.validators import RegexValidator


class Orders(models.Model):

    STATUS = (
        ('new', 'Новый'),
        ('done', 'Оформлен'),
        ('denyed', 'Отменен')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=30, verbose_name='Имя', null=True)
    first_name = models.CharField(max_length=30, verbose_name='Фамилия', null=True)
    email = models.EmailField(verbose_name='Электронная почта', null=True)
    phone_regex = RegexValidator(regex=r'(\+996)\(\d{3}\)\d{2}-\d{2}-\d{2}', message="Phone number must be entered in the format: '+996(700)12-34-56'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='+996(700)12-34-56', verbose_name='Номер телефона')
    country = models.CharField(max_length=30, verbose_name='Страна', null=True)
    city = models.CharField(max_length=255, verbose_name='Город', null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления', null=True)
    status = models.CharField(max_length=30, choices=STATUS, default='new', verbose_name='Статус заказа')

    def __str__(self):
        return f'{self.name} {self.first_name}'
    
    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

 
class Order_check(models.Model):
    client = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True, related_name='order')
    quantity_line = models.IntegerField(verbose_name='Количество линеек')
    quantity = models.IntegerField(verbose_name='Количество товара')
    price = models.FloatField(verbose_name='Сумма')
    discount = models.FloatField(verbose_name='Скидка')
    final_price = models.FloatField(verbose_name='Итого к оплате')

    def __str__(self):
        return str(self.id)

    def get_final_price(self):
        return self.final_price

    class Meta:
        verbose_name = 'Чек'
        verbose_name_plural = 'Чек'
    

class Product_to_Order(models.Model):
    client = models.ForeignKey(Order_check, on_delete=models.CASCADE, null=True, related_name='product')
    image = models.ImageField(verbose_name='Фотография')
    color = ColorField(default='#fff', verbose_name='Цвет')
    name = models.CharField(max_length=255, verbose_name='Название')
    size_range = models.CharField(max_length=20, verbose_name='Размерный ряд')
    price = models.IntegerField(verbose_name='Цена')
    new_price = models.FloatField(verbose_name='Цена после скидки')
    quantity = models.IntegerField(verbose_name='Количество товара')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Продукты'
        verbose_name_plural = 'Продукты'
        