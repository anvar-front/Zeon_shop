from tabnanny import verbose
from django.db import models
from ckeditor.fields import RichTextField
from django.core.validators import RegexValidator

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
        return f"Слайдер {self.id}"
    
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


class Call_back(models.Model):

    CHOICES = (
        ('1', 'Нет'),
        ('2', 'Да')
    )

    name = models.CharField(max_length=255)

    phone_regex = RegexValidator(regex=r'(\+996)\(\d{3}\)\d{2}-\d{2}-\d{2}', message="Phone number must be entered in the format: '+996(700)12-34-56'.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, default='+996(700)12-34-56')

    date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=255)
    status = models.CharField(max_length=5,  choices = CHOICES, default=1)

    def __str__(self):
        return f'Звонок клиента: {self.name} в {self.date}'
    
    class Meta:
        verbose_name = 'Обратный звонок'
        verbose_name_plural = 'Обратные звонки'


class Footer_first_side(models.Model):
    logo = models.ImageField()
    info = models.TextField()
    number = models.IntegerField()

    def __str__(self):
        return 'Footer'

    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footer'


class Footer_second_side(models.Model):
    SOCIAL = (
        ('phone', 'phone'),
        ('email', 'email'),
        ('instagram', 'instagram'),
        ('telegram', 'telegram'),
        ('whatsapp', 'whatsapp')
    )

    social = models.CharField(max_length=255, choices=SOCIAL)
    link = models.TextField()
    footer = models.ForeignKey(Footer_first_side, on_delete=models.CASCADE, related_name='link', null=True, blank=True, default=None)

    def save(self):
        if self.social == 'whatsapp':
            self.link = 'https://wa.me/'+self.link
        super(Footer_second_side, self).save()


    def __str__(self):
        return self.social
