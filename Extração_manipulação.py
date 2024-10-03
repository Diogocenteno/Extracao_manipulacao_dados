#Extração e manipulação de dados


import requests
from bs4 import BeautifulSoup

# Desabilitar avisos de segurança
requests.packages.urllib3.disable_warnings()

# URL do site
url = 'https://books.toscrape.com/'
requisicao = requests.get(url)
requisicao.encoding = 'utf-8'

# Extrair o conteúdo da página
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Inicializar variáveis
contar_livros = 0
catalogo = []

# Encontrar todas as tags <article> que contêm os livros
for artigo in extracao.find_all('article'):
    livro = {}

    # Encontrar o título do livro extraindo o texto da tag <a>
    titulo = artigo.find('h3').find('a').text
    livro['Título'] = titulo  # Armazenar o título completo

    # Encontrar o preço do livro
    preco = artigo.find('p', class_='price_color').text
    livro['Preço'] = preco

    # Adicionar o livro ao catálogo
    catalogo.append(livro)

    # Incrementar a contagem de livros
    contar_livros += 1

# Imprimir a quantidade de livros
print(f'Quantidade de livros: {contar_livros}')

# Mostrar os livros
for livro in catalogo:
    print(f'Título: {livro["Título"]}, Preço: {livro["Preço"]}')