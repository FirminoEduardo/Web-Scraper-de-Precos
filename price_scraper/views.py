from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo ao Web Scraper de Preços!")