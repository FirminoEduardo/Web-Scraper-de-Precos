from django.shortcuts import render, redirect
from .models import Produto
from .forms import ProdutoForm

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

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'liga_produtos.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
        else:
            form = ProdutoForm()
        return render(request, 'adicionar_produto.html', {'form': form})
    
def remover_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete
    return redirect('lista_produtos')
