from django.db import models
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shops'

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(max_length=120, db_index=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='shop')
    shop = models.ForeignKey('Shop', on_delete=models.PROTECT, related_name='item')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class Price(models.Model):
    price = models.IntegerField()
    date = models.DateField(default=timezone.now)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='price')

    def __str__(self):
        return str(self.price)

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'


