from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DeleteView

from .models import Product


class Index(ListView):
    template_name = 'shop/products.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        queryset = queryset.order_by('price')

        return queryset


class ShowProduct(DeleteView):
    model = Product
    template_name = 'shop/certain_product.html'
    context_object_name = 'product'
