from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255) # Nome do produto
    url = models.URLField() # Url do produto
    preco_atual = models.DecimalField(max_digits=10, decimal_places=2) # Preço atual do produto
    ultima_atualizacao = models.DateTimeField(auto_now=True) # Data e hora da última atualização de preço

    def __str__(self):
        return self.nome # Exibe o nome do produto como String