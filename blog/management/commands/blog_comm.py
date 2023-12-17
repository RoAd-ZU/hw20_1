import psycopg2
from django.core.management import BaseCommand

from blog.models import Blog


class Command(BaseCommand):

    def handle(self, *args, **options):
        Blog.objects.all().delete()