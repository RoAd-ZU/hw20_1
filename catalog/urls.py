from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import base, data, description

app_name = CatalogConfig.name

urlpatterns = [
    path('', data, name='data'),
    path('desc/<int:pk>', description, name='desc')
]