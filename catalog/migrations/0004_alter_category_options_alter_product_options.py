# Generated by Django 4.2.7 on 2023-11-27 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_category_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',)},
        ),
    ]
