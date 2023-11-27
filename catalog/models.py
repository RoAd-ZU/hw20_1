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

    def __str__(self):
        return f'{self.name} | описание: {self.description}\n {self.category}\n {self.price}'

    class Meta:
        ordering = ('name',)

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.name} | описание: {self.description}'

    class Meta:
        ordering = ('name',)