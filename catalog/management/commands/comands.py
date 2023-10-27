from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        products_list = [
            {'name':'змея', 'description':'ужужужужуж', 'image':'', 'category':'от ежа', 'price':1, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'},
            {'name':'змея', 'description':'ужужужужуж', 'image':'', 'category':'от ежа', 'price':2, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'},
            {'name':'змея', 'description':'ужужужужуж', 'image':'', 'category':'от ежа', 'price':12, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'},
            {'name':'змея', 'description':'ужужужужуж', 'image':'', 'category':'от ежа', 'price':21, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'}
        ]

        products_cr = []
        for item in products_list:
            products_cr.append(Product(**item))

        Product.objects.bulk_create(products_cr)
