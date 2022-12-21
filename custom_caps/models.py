from django.db import models
# from discounts.models import MagazineDiscount
from user.models import CustomUser


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'categories'
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category, related_name='brands')
    image = models.ImageField(upload_to='static', blank=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    SIZE_CHOICES = (
        ('Small', 'S'),
        ('Medium', 'M'),
        ('Large', 'L'),
        ('eXtra Large', 'XL')
    )
    name = models.CharField(choices=SIZE_CHOICES, max_length=30, null=False)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    country_of_origin = models.CharField(blank=True, null=True, max_length=50, verbose_name="Страна производства")

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class Caps(models.Model):
    CURRENCY_CHOICES = (
        ('USD', 'DOLLAR'),
        ('KGS', 'SOM'),
        ('TENGE', 'TENGE'),
    )
    # discount = models.OneToOneField(MagazineDiscount, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection,
                                   on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, unique=True, verbose_name="Название")
    buyer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name="Покупатель")
    categories = models.ManyToManyField(Category, related_name='caps')
    sizes = models.ManyToManyField(Size, related_name='size')
    image = models.ImageField(null=True, blank=True, verbose_name="Фотография")
    manufacturer = models.ForeignKey(Manufacturer,
                                     related_name='Shops',
                                     on_delete=models.CASCADE, verbose_name="Производитель")
    currency = models.CharField(max_length=100, choices=CURRENCY_CHOICES,
                                default='kgz', verbose_name="Валюта")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")

    class Meta:
        ordering = ('name',)

    def count(self):
        return self.sizes.count()

    def brand_name(self):
        return self.brand.name

    def get_name(self):
        name = self.name if self.name else self.collection.name
        return name

    def description(self):
        return self.collection.description

    def __str__(self):
        return f'ID {self.id}: {self.name}'


class UserCapsRelation(models.Model):
    RATING_CHOICES = (
        (1,  'Нормально'),
        (2, 'Хорошо'),
        (3, 'Отлично'),
        (4, 'Прекрасно'),
        (5, 'Изумительно')
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Пользователь")
    caps = models.ForeignKey(Caps, on_delete=models.CASCADE, verbose_name="Кепка")
    like = models.BooleanField(default=False, verbose_name="Нравится")
    favorites = models.BooleanField(default=False, verbose_name="Избранное")
    rate = models.PositiveSmallIntegerField(choices=RATING_CHOICES, null=True, verbose_name="Оценка")

    def __str__(self):
        return f'ID {self.id}: {self.user}: {self.caps.name}'
