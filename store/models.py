from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Phone(models.Model):
    phone_text = models.CharField(max_length=255, verbose_name='номер телефона')

    def __str__(self):
        return self.phone_text

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    phone = models.ForeignKey(Phone, verbose_name='Номер', on_delete=models.CASCADE)

    is_published = models.BooleanField(verbose_name='Запущен на сайте?')
    slug = models.SlugField(unique=True)
    full_title = models.TextField(verbose_name='TITLE Название Страницы Сайта')
    meta_description = models.TextField(verbose_name='МетаТег Описания')
    alt = models.TextField(verbose_name='Описание того, что изображено на картинке (название товара)')
    
    category = models.ForeignKey(Category, verbose_name='Категория товара', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Полное название продукта')
    short_title = models.CharField(max_length=255, verbose_name='Краткое название, если основное очень длинное')
    
    mini_image = models.ImageField(verbose_name='Изображение 400x350 для главной страницы', upload_to=f'product_photos/400x350')
    image = models.ImageField(verbose_name='Изображение 600х600', upload_to=f'product_photos/600x600')
    short_description = models.TextField(verbose_name='Краткое описание для главной страницы (до 100 символов)')
    description = models.TextField(verbose_name='Описание товара подробноее не очень большое для начала')

    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')

    # table
    active_substance = models.CharField(verbose_name='Действующее вещество', max_length=100)
    manufacturer = models.CharField(verbose_name='Производитель', max_length=100)
    release_form = models.CharField(verbose_name='Форма выпуска', max_length=100)
    packaging = models.CharField(verbose_name='Код ATX', max_length=100)
    qty_in_a_package = models.CharField(verbose_name='Кол-во в упаковке', max_length=100)

    full_description = models.TextField(verbose_name='Большой текст описания')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product", kwargs={"product_slug": self.slug})
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']
            