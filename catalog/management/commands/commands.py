import psycopg2
from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        conn = psycopg2.connect(host='localhost', database='hw20_1', user='postgres')
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('TRUNCATE TABLE catalog_product RESTART IDENTITY CASCADE')


        finally:
            conn.close()
        products_list = [
            {'name':'змея', 'description':'ужужужужуж', 'image':'media/Snake.jpg', 'category':'от ежа', 'price':100, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'},
            {'name':'чупачупс', 'description':'погрызен, упакован', 'image':'media/Chupa.jpg', 'category':'набор педофила', 'price':45, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'},
            {'name':'плавки-невидимки', 'description':'свобода движений и ветер щекочет', 'image':'media/Hmm.jpg', 'category':'шнурки пляжные', 'price':12000, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'},
            {'name':'электромолоток подвесной (чугунный)', 'description':'доп.комплектация к будильнику "Последний рассвет"', 'image':'media/Hummer.jpg', 'category':'доброе утро', 'price':2100, 'date_cr':'1555-12-12', 'date_ch':'1555-12-12'}
        ]

        Category.objects.all().delete()
        conn = psycopg2.connect(host='localhost', database='hw20_1', user='postgres')
        try:
            with conn:
                with conn.cursor() as cursor:
                    cursor.execute('TRUNCATE TABLE catalog_category RESTART IDENTITY CASCADE')


        finally:
            conn.close()
        category_list = [
            {'name':'от ежа', 'description':'от ежа ежам ежовое'},
            {'name':'набор педофила', 'description':'чупачупсы и презервативы'},
            {'name':'шнурки пляжные', 'description':'современные модные купальные костюмы ультра-бикини'},
            {'name':'доброе утро', 'description':'уведомляторы о зарплате, празднике, внеплановом выходном'}
        ]

        products_cr = []
        for item in products_list:
            products_cr.append(Product(**item))

        category_cr = []
        for item in category_list:
            category_cr.append(Category(**item))

        Product.objects.bulk_create(products_cr)
        Category.objects.bulk_create(category_cr)
