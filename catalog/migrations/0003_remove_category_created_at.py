# Generated by Django 4.2.6 on 2023-10-25 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_category_created_at_alter_product_date_ch_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='created_at',
        ),
    ]
