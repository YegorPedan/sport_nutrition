from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Product


class Index(ListView):
    template_name = 'shop/products.html'
    model = Product
    context_object_name = 'products'
