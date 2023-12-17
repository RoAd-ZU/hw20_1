from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='slug', **NULLABLE)
    content = models.CharField(max_length=555, verbose_name='содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='превью', **NULLABLE)
    date_cr = models.DateField(verbose_name='дата создания', **NULLABLE)
    publication_sign = models.BooleanField(default=True, verbose_name="опубликовано")
    views_counter = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return f'{self.title} {self.content} {self.preview} {self.slug}'

    class Meta:
        ordering = ('title',)