from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'shop/base.html'