from django.contrib import admin
from django.urls import path
from . import views  # Importando as views da app scraper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Rota para a página inicial
    path('atualizar_precos/', views.atualizar_precos, name='atualizar_precos'), # Rota para atualizar precos
    path('', views.lista_produtos, name='lista_produtos'), # Rota para listar produtos 
    path('adicionar/', views.adicionar_produto, name='adicionar_produto'), # Rota para adicionar um produto
    path('remover/<int:produto_id>/', views.remover_produto, name='remover_produto'), # Rota para remover um produto
]