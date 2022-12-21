from django.db import models
from custom_caps.models import Caps, Category


class MagazineDiscount(models.Model):
    discount_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name="Cумма скидки")
    minimum_purchased_items = models.IntegerField(null=False, verbose_name="Минмимальное количество купленных товаров")
    target_caps = models.ForeignKey(Caps, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="target")
    target_category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="target")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано в")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено в")

    def __str__(self):
        return f'ID {self.id}: ({self.discount_amount})'


