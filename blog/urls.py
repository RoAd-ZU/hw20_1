from django.urls import path

from blog.apps import BlogConfig
from blog.views import DataListView, DescriptionDetailView, BlogCreateView, BlogUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('', DataListView.as_view(), name='data'),
    path('blog/', BlogCreateView.as_view(), name='create'),
    path('desc/<int:pk>', DescriptionDetailView.as_view(), name='desc'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update')
]