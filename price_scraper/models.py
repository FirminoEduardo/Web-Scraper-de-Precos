from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255) # Nome do produto
    url = models.URLField() # Url do produto
    preco_atual = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True) # Preço atual do produto
    preco_desejado = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True) # Data e hora da última atualização de preço

    def __str__(self):
        return self.nome # Exibe o nome do produto como String
    
class HistoricoPreco(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produto.nome} - {self.preco} - {self.data}"