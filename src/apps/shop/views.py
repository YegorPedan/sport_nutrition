from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from .models import Product


class Index(ListView):
    template_name = 'shop/products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3


class ShowProduct(DeleteView):
    model = Product
    template_name = 'shop/certain_product.html'
    context_object_name = 'product'
