from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    image = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_cr = models.DateField(verbose_name='дата создания', **NULLABLE)
    date_ch = models.DateField(verbose_name='дата последнего изменения', **NULLABLE)

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')
    created_at = models.CharField(max_length=50, verbose_name='будет отменено', **NULLABLE)

class Meta:
    ordering = ('name',)