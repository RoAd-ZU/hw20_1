from django.views.generic import ListView, DetailView

from catalog.models import Product
from django.shortcuts import render


class BaseListView(ListView):
    model = Product
    template_name = 'catalog/base.html'


class DataListView(ListView):
    model = Product
    template_name = 'catalog/data.html'


class DescriptionDetailView(DetailView):
    model = Product
    template_name = 'catalog/desc.html'

# def base(request):
#     Product_list = Product.objects.all()
#     content = {
#         'object_list': Product_list,
#         'title': 'Каталог',
#         'description': 'Ну тут всё прям для тебя',
#     }
#     return render(request, 'catalog/base.html', content)

# def data(request):
#     Product_list = Product.objects.all()
#     content = {
#         'object_list': Product_list,
#         'title': 'Каталог',
#         'description': 'Ну тут всё прям для тебя',
#     }
#     return render(request, 'catalog/data.html', content)

# def description(request, pk):
#     Description_list = Product.objects.get(pk=pk)
#     content = {
#         'object_list': Description_list,
#         'title': 'Описание',
#         'description': 'Коротко и понятно'
#     }
#     return render(request, 'catalog/desc.html', content)