from tabnanny import verbose
from ckeditor.fields import RichTextField
from django.db import models


class News(models.Model):
    """
    Модель для новостей
    """
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = RichTextField(verbose_name='Текст')
    image = models.ImageField(upload_to='news/', verbose_name='Фотография')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'    
        verbose_name_plural = 'Новости'    

    