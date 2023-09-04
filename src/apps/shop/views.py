from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
   def get(self, request):
      return HttpResponse('Hallo, world')