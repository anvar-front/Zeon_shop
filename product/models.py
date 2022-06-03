from email.policy import default
from django.db import models
from colorfield.fields import ColorField
from ckeditor.fields import RichTextField
import math


class  Collection(models.Model):        # Коллекция
    image = models.ImageField(upload_to='collection/')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'



class Product(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    vendor_code = models.CharField(max_length=255)      # артикул товара
    price = models.IntegerField()
    discount = models.IntegerField(null=True,blank=True, default=0)
    new_price = models.FloatField(null=True, blank=True, default=0)
    description = RichTextField()
    size_range = models.CharField(max_length=20)
    fabric_structure = models.CharField(max_length=255)     # состав ткани
    quantity = models.IntegerField(null=True, blank=True, default=5)
    material = models.CharField(max_length=255)
    bestseller = models.BooleanField(default=False)
    new = models.BooleanField(default=True)
    favorite = models.BooleanField(default=False)

    def save(self):
        if self.discount != 0:
            self.new_price = self.price - ((self.price * self.discount) / 100)
        else:
            self.new_price = self.price

        self.quantity = math.floor(((int(self.size_range[3:]) - int(self.size_range[:2])) / 2)) + 1
        super(Product, self).save()



class Image_color(models.Model):
    image = models.ImageField(upload_to='product/')
    color = ColorField(default='#fff')
    image_color = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

    def __str__(self):
        return f'Image: {self.image} -  Color: {self.color}'
    







