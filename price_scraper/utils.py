import requests

from bs4 import BeautifulSoup

def obter_preco(url):
    ''''
        Função para obter o preço do produto de uma página web
        Esta função deve ser adaptada para cada site, dependendo da estrutura HTML do site
    '''

    headers = {"User-Agent": "Mozilla/5.0"} # Header para evitar bloqueios
    response = requests.get(url, headers=headers)

    #Verificar se a requisição foi bem-sucedida
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Exemplo de como encontrar o preço - Precisa ser adaptado para o site específico
        preco_elemento = soup.find('span', {'class': 'price'}) # Mudar conforme a estrutura do site

        if preco_elemento:
            preco = preco_elemento.text.strip()
            return preco
        else:
            return None
    else:
        return None