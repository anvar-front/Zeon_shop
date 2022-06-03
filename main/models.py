from distutils.command.upload import upload
from django.db import models
from ckeditor.fields import RichTextField


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextField()

    def __str__(self):
        return 'О нас'

    class Meta:
        verbose_name_plural = 'О нас'
        verbose_name = 'О нас'


class AboutUsImage(models.Model):
    aboutus = models.ForeignKey(AboutUs, on_delete=models.CASCADE, related_name='about_img', blank=True, null=True, default=None)
    image = models.ImageField(upload_to='about_us/')
    is_active = models.BooleanField(default=False)
    is_main = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return  '%s' % self.image

    class Meta:
        verbose_name = 'Фотография'    
        verbose_name_plural = 'Фотографии'    


class Advantage(models.Model):      # наши преимущества
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to='advantage/')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Наше преимущество'
        verbose_name_plural = 'Наши преимущества'


class PublicOffer(models.Model):
    title = models.CharField(max_length=255, null=True)
    text = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публичная оферта'
        verbose_name_plural = 'Публичная оферта'


class Slider(models.Model):
    link = models.URLField(null=True)
    image = models.ImageField(upload_to='slider/', null=True)

    def __str__(self):
        return "Слайдер"
    
    class Meta:
        verbose_name = 'Слайдер'
        verbose_name_plural = 'Слайдер'


class Help_img(models.Model):
    image = models.ImageField(upload_to='help/')

    def __str__(self):
        return 'Помощь'

    class Meta:
        verbose_name = 'Фотография для помощи'
        verbose_name_plural = 'Фотография для помощи'


class Help(models.Model):
    image = models.ForeignKey(Help_img, on_delete=models.CASCADE, related_name='questions', null=True)
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = 'Помощь'
        verbose_name_plural = 'Помощь'


