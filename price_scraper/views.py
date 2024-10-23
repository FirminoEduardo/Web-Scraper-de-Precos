from django.shortcuts import render

# Create your views here.
from .models import Produto
from .utils import obter_preco
from django.http import HttpResponse

def atualizar_precos(request):
    produtos = Produto.objects.all() # Pegar todos os produtos cadastrados
    for produto in produtos:
        preco = obter_preco(produto.url) # Obter o preço atualizado
        if preco:
            produto.preco_atual =  preco # Atualizar o preço no banco de dados
            produto.save() # Salvar alteração
    return render(request, 'atualizar_precos.html', {'produtos': produtos})


def home(request):
    return HttpResponse("Bem-vindo ao Web Scraper de Preços!")