from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import DataListView, DescriptionDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', DataListView.as_view(), name='data'),
    path('desc/<int:pk>', DescriptionDetailView.as_view(), name='desc'),
]