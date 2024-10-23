from django.contrib import admin
from django.urls import path
from price_scraper import views  # Importando as views da app scraper

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Rota para a página inicial
    path('atualizar_precos/', views.atualizar_precos, name='atualizar_precos') # Rota para atualizar precos
]