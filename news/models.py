from django.db import models
from ckeditor.fields import RichTextField


class News(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()
    image = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'    
        verbose_name_plural = 'Новости'    

    