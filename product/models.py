from django.db import models
from django.core.exceptions import ValidationError
import math

from colorfield.fields import ColorField
from ckeditor.fields import RichTextField

from user.models import User


class Collection(models.Model):
    """
    Модель дл коллекции
    """
    image = models.ImageField(upload_to='collection/',
                              verbose_name='Фотография')
    title = models.CharField(max_length=255, verbose_name='Наименование')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


def size_validate(size):
    """
    Функция для валидации размеров товара (42-50)
    """
    if size[:2].isdigit() and size[3:].isdigit() and size[2] == '-':
        return True
    else:
        raise ValidationError('Введите валидное значение')


class Product(models.Model):
    """
    Модель для товара
    """
    collection = models.ForeignKey(Collection,
                                   on_delete=models.CASCADE,
                                   related_name='products',
                                   verbose_name='Коллекция')
    name = models.CharField(max_length=255, verbose_name='Наименование')
    vendor_code = models.CharField(max_length=255, verbose_name='Артикул')
    price = models.IntegerField(verbose_name='Цена')
    discount = models.IntegerField(null=True,
                                   blank=True,
                                   default=0,
                                   verbose_name='Скидка')
    new_price = models.FloatField(null=True,
                                  blank=True,
                                  default=0,
                                  verbose_name='Цена после скидки')
    description = RichTextField(verbose_name='Описание')
    size_range = models.CharField(max_length=5,
                                  verbose_name='Размерный ряд',
                                  help_text='Пример: 42-50',
                                  validators=[size_validate])
    fabric_structure = models.CharField(max_length=255,
                                        verbose_name='Состав ткани')
    quantity = models.IntegerField(null=True,
                                   blank=True,
                                   default=0,
                                   verbose_name='Количество')
    material = models.CharField(max_length=255, verbose_name='Материал')
    bestseller = models.BooleanField(default=False, verbose_name='Хит продаж')
    new = models.BooleanField(default=True, verbose_name='Новый')

    def save(self):
        if self.discount != 0:
            self.new_price = self.price - ((self.price * self.discount) / 100)
        else:
            self.new_price = self.price

        size = self.size_range.split("-")
        self.quantity = math.floor(((int(size[1]) - int(size[0])) / 2)) + 1
        super(Product, self).save()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Image_color(models.Model):
    """
    Фотография и цвет товара (связаны)
    """
    image = models.ImageField(upload_to='product/', verbose_name='Фотография')
    color = ColorField(default='#fff', verbose_name='Цвет')
    image_color = models.ForeignKey(Product,
                                    on_delete=models.CASCADE,
                                    related_name='images')

    def __str__(self):
        return f'Image: {self.image} -  Color: {self.color}'


class Favorite(models.Model):
    """
    Избранные товары авторизованного юзера
    """
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='favorite_products')
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='favorite_user')
